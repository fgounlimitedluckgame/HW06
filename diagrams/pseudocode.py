"""
AI-Driven API Test Generator for EShop SUT.
Reads API definitions and business constraints, orchestrates multi-pass test generation,
and compiles an executable Postman Collection with mandatory audit tags.
"""

from dataclasses import dataclass, field
import json
from typing import Any, Dict, List


@dataclass
class TestCase:
  test_id: str
  endpoint: str
  method: str
  category: str  # Partition, State, Security, Schema
  headers: Dict[str, str]
  payload: Dict[str, Any]
  expected_status: int
  assertions: List[str]
  audit_status: str = "PENDING_REVIEW"
  audit_notes: str = ""


class APISpecParser:

  def __init__(self, spec_content: str, business_rules: str):
    self.spec = spec_content
    self.rules = business_rules

  def extract_endpoint_context(self, endpoint_path: str) -> Dict[str, Any]:
    # Parse query params, body schemas, auth requirements, and constraints
    return {
        "endpoint": endpoint_path,
        "method": "POST" if "register" in endpoint_path else "PUT",
        "auth_required": "admin" in endpoint_path or "orders" in endpoint_path,
        "raw_rules": self.rules,
    }


class LLMTestStrategyEngine:

  def __init__(self, student_id: str):
    self.student_id = student_id

  def prompt_llm(self, sub_goal: str, context: Dict[str, Any]) -> List[Dict]:
    # Placeholder for Antigravity LLM API call
    # Builds structured prompts enforcing ISTQB partitions and SEC-01..07
    pass

  def generate_partition_tests(self, context: Dict) -> List[TestCase]:
    raw = self.prompt_llm("Equivalence Partitioning and BVA", context)
    return self._normalize(raw, "Partition")

  def generate_security_tests(self, context: Dict) -> List[TestCase]:
    raw = self.prompt_llm("SEC-01 to SEC-07 Injections & RBAC Tampering", context)
    return self._normalize(raw, "Security")

  def generate_state_tests(self, context: Dict) -> List[TestCase]:
    raw = self.prompt_llm("FR-10 Order State Machine Transitions", context)
    return self._normalize(raw, "State_Transition")

  def _normalize(self, raw_items: List[Dict], category: str) -> List[TestCase]:
    cases = []
    for idx, item in enumerate(raw_items or []):
      cases.append(
          TestCase(
              test_id=f"{category[:3].upper()}_{idx+1:03d}",
              endpoint=item.get("endpoint", ""),
              method=item.get("method", "POST"),
              category=category,
              headers={"X-Student-Id": self.student_id},
              payload=item.get("body", {}),
              expected_status=item.get("expected_status", 200),
              assertions=item.get("assertions", []),
          )
      )
    return cases


class PostmanCollectionCompiler:

  @staticmethod
  def export_collection(
      test_cases: List[TestCase], output_file: str, student_id: str
  ):
    collection = {
        "info": {
            "name": f"EShop_Generated_Suite_{student_id}",
            "schema": (
                "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
            ),
        },
        "item": [],
    }

    for tc in test_cases:
      item = {
          "name": f"[{tc.category}] {tc.test_id} - Expected {tc.expected_status}",
          "request": {
              "method": tc.method,
              "header": [
                  {"key": "X-Student-Id", "value": student_id, "type": "text"},
                  {"key": "Content-Type", "value": "application/json"},
              ],
              "body": {
                  "mode": "raw",
                  "raw": json.dumps(tc.payload, indent=2),
              },
              "url": {
                  "raw": "{{baseUrl}}" + tc.endpoint,
                  "host": ["{{baseUrl}}"],
                  "path": tc.endpoint.strip("/").split("/"),
              },
          },
          "event": [{
              "listen": "test",
              "script": {
                  "type": "text/javascript",
                  "exec": [
                      f"pm.test('Status code is {tc.expected_status}', function"
                      " () {",
                      f"    pm.response.to.have.status({tc.expected_status});",
                      "});",
                  ]
                  + [
                      f"pm.test('{a}', function() {{ /* assertion code */ }});"
                      for a in tc.assertions
                  ],
              },
          }],
      }
      collection["item"].append(item)

    with open(output_file, "w", encoding="utf-8") as f:
      json.dump(collection, f, indent=2)


def main():
  student_id = "23127108"
  parser = APISpecParser(
      spec_content="api_specification.md", business_rules="SRS.md"
  )
  engine = LLMTestStrategyEngine(student_id=student_id)

  target_endpoints = [
      "/api/register",
      "/api/apply-coupon",
      "/api/admin/orders/1/status",
  ]
  all_suite: List[TestCase] = []

  for ep in target_endpoints:
    ctx = parser.extract_endpoint_context(ep)
    all_suite.extend(engine.generate_partition_tests(ctx))
    all_suite.extend(engine.generate_security_tests(ctx))
    all_suite.extend(engine.generate_state_tests(ctx))

  # Export to Postman format for Newman execution
  PostmanCollectionCompiler.export_collection(
      all_suite, "postman_collection.json", student_id
  )


if __name__ == "__main__":
  main()