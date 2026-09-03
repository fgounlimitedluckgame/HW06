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

* Số API đã test: 3 (`/api/register`, `/api/cart`, `/api/categories`)

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

## 4. Cách chạy collection: 
- Trước khi chạy API, chạy backend trước băng lệnh `node server.js`
- Chạy trên GUI:
    - Chạy trước 2 API request trong folder `prerequisite folders` để lấy token user và admin
    - Sau đó, chạy API trong folder `API Test suite` bằng cách đưa dữ liệu từ file `csv` vào trong test (dữ liệu có sẵn trong tập tin `test_data`)
- Chạy trên CLI:
    - Chạy trước lệnh `npm install -g newman newman-reporter-htmlextra` để có thể tạo newman report
    - Chạy 2 api để lấy token user và admin:
    ```bash
    newman run hw06.postman_collection.json --folder "prerequisite folders" -e hw06.postman_environment.json --export-environment hw06.postman_environment.json
    ```
    - Chạy test suite và xuất newman report:
    ```bash
    newman run hw06.postman_collection.json --folder "API Test suite" -e hw06.postman_environment.json -d <đường dẫn file csv> -r cli -r htmlextra --reporter-htmlextra-export /reports/<tên báo cáo>.html
    ```

---

## 5. Ghi chú
- Chi tiết test case được lưu trong các workbook excel trong thư mục `workbooks`
- Test data csv được lưu trong thư mục `test_data`
- Biểu đồ và pseudocode được lưu trong thư mục `diagrams`
- Hình ảnh bug được lưu trong thư mục `bug_screenshots`
- Hình ảnh minh hoạ CI/CD được lưu trong thư mục `ci_cd`
- `ci_tests` là thư mục dùng để thêm file csv để test CI/CD (để trống, nếu muốn test thì chỉ đưa một file duy nhất, test xong một file thì xoá file đó ngay lập tức nếu muốn test file tiếp theo)
- Báo cáo newman được lưu trong thư mục `newman_reports`