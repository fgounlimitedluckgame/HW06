# AI Audit Report

This document logs the interactions with the AI assistant during the test suite generation for HW06.

---

### Interaction 1: Test Cases Generation Design and Execution

- **AI tool name:** Antigravity
- **Date/Time**: 2026-08-27T22:46:15+07:00 to 2026-08-27T22:48:52+07:00
- **User prompt**: 
  > for this homework, generate 35 API test cases for each following FRs: FR-01: Account Registration (Pool A), FR-07: Shopping Cart (Pool B), FR-15: Product CRUD (Pool C)
  > note:
  > - read the api_specification.md file in references to get the API endpoints, do not fabricate them
  > - abide to the homework requirement to make sure the test suite cover: domain partitions on every parameter, state transitions, security, and schema validation
  > - do not manually add 5 more test cases for the FRs. Only generate 35, the last 5 will be human added
- **Output summary**: 
  - Generated exactly **105 API test cases** (35 cases for each requested FR: FR-01, FR-07, and FR-15).
  - Maintained structured metadata for each case containing: `Test_ID`, `Category` (Partition, Security, State, Schema), `Request_Payload`, `Expected_Status`, `Schema_Validation`, and `Assertion_Script`.
  - Saved the generated test cases to [`api_test_cases_generation.md`](file:///c:/Users/Huong%20Ly/Documents/hw06_api%20-%20Copy/api_test_cases_generation.md).
- **Human review or correction**: 
Đã bỏ qua assertion script được viết bằng pseudocode ở một số state transition test, và đánh dấu những case đó là `INCOMPLETE` 

---

### Interaction 2: Thêm script duyệt file csv cho file ci
- **AI tool name**: Gemini
- **Date/Time**: 31/8/2026 22:41
- **User prompt**:
`name: Run Newman on All CSV Test Suites run: | mkdir -p ./reports for file in *_test_cases.csv; do suite_name=$(basename "$file" .csv) echo "==================================================" echo "Executing Suite: $suite_name ($file)" echo "==================================================" newman run postman_collection.json \ -d "$file" \ --environment postman_environment.json \ --reporters cli,htmlextra \ --reporter-htmlextra-export "./reports/${suite_name}-report.html" done so this one checks the test case files everywhere, even the one stored in folder? (I asked it so I can store my main csv test case files in a folder (not used for testing), while the clone test files is committed outside)`
- **Output summary:** Đã gợi ý cách duyệt file csv để test trên ci
- **Human review or correction**: Không có

### Interaction 3: Thêm script duyệt file csv cho file ci
- **AI tool name**: Gemini
- **Date/Time**: 29/8/2026 15:49
- **User prompt**:
`a complete configuration, from environment variables to the request configuration`
- **Output summary:** Đã tạo các cài đặt trên postman: environment variables, pre-request và post-request script
- **Human review or correction**: Đã thêm vào các biến còn thiếu ở environment, post-request script

### Interaction 4: Sinh flowchart và pseudocode cho kiểm thử API
- **AI tool name**: Gemini
- **Date/Time**: 27/8/2026 13:38
- **User prompt**:
` for this homework, how to do it, and also give me agent skill(s) for this homework (the AI agent is run on Antigravity) and also give me relevant pseudocodes (can be in python) , a mermaid diagram in text for the AI-driven API test generator for the SUT (given the API specification, it produces test cases automatically)`
- **Output summary:** Đã tạo flowchart bằng mermaid + pseudocode python
- **Human review or correction**: Đã review lại mermaid flowchart và pseudocode, sau đó chấp nhận artifact
