# HW06

---

## 1. Test summary report

- **Danh sách test case:**

| API | AI-generated | Manual extension | Tổng | `VALID` | `INCOMPLETE` | `INVALID` |
|---|---:|---:|---:|---:|---:|---:|
| FR-01 | 35 | 5 | 40 | 38 | 2 | 0 |
| FR-07 | 35 | 5 | 40 | 35 | 5 | 0 |
| FR-15 | 35 | 5 | 40 | 36 | 4 | 0 |
| **Tổng** | **105** | **15** | **120** | **109** | **11** | **0** |

- **Các test case `INCOMPLETE`**:
    - FR01: `FR01-ST-029` và `FR01-ST-030`
    - FR07: `FR07-ST-024` đến `FR07-ST-028`
    - FR15: `FR07-ST-024` đến `FR07-ST-027`

- **Kết quả kiểm thử:**

| API | Scenario rows | Passed rows | Failed rows |
|---|---:|---:|---:|
| FR-01 | 40 (35 + 5) | 11 | 29 |
| FR-08 | 40 (35 + 5) | 13 | 27 |
| FR-15 | 40 (35 + 5) | 15 | 25 |
| **Tổng** | **120** | **39** | **81** |

* Số lượng bug phát hiện: 7 (xem chi tiết bug tại [bug_report.md](bug_report.md))

---

## 2. Bảng đánh giá
| STT | Tiêu chí | Điểm tối đa | Điểm tự đánh giá |
|---|---|---:|---:|
| 1 | API 1 – full pipeline | 30 | `30` |
| 2 | API 2 – full pipeline | 30 | `30` |
| 3 | API 3 – full pipeline | 30 | `30` |
| 4 | Agent Skill – AI-driven test generator | 10 | `10` |
| | **Tổng** | **100** | **`100`** |

---

## 3. Demo video
* Demo AI agent: https://youtu.be/hShyjP6HiGY

---

## 4. Ghi chú
- Chi tiết test case được lưu trong các workbook excel trong thư mục `workbooks`
- Test data csv được lưu trong thư mục `test_data`
- Biểu đồ và pseudocode được lưu trong thư mục `diagrams`
- Hình ảnh bug được lưu trong thư mục `bug_screenshots`
- Hình ảnh minh hoạ CI/CD được lưu trong thư mục `ci_cd`
- `ci_tests` là thư mục dùng để thêm file csv để test CI/CD (để trống, nếu muốn test thì chỉ đưa một file duy nhất, test xong một file thì xoá file đó ngay lập tức nếu muốn test file tiếp theo)
- Báo cáo newman được lưu trong thư mục `newman_reports`