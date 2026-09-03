# BÁO CÁO TÍCH HỢP CI/CD (CI/CD REPORT)
**Hệ thống:** EShop API Automation Testing  
**Học phần:** Kiểm thử Phần mềm (HW06 – API Testing)  
**Mã sinh viên:** 23127108  
**Công cụ CI/CD:** GitHub Actions + Newman CLI + HTML Extra Reporter  

---

## 1. Cấu hình CI/CD

Pipeline CI/CD được thiết lập thông qua tệp tin `.github/workflows/api-tests.yml`, tự động kích hoạt mỗi khi có sự kiện `push` hoặc `pull_request` lên nhánh chính (`main`/`master`). CI/CD hỗ trợ kiểm thử thủ công qua `workflow-dispatch`

### Các bước thực thi trong Pipeline:
1. **Checkout Code:** Tải mã nguồn repository về môi trường máy ảo `ubuntu-latest`.
2. **Setup Node.js:** Thiết lập môi trường Node.js phiên bản 20 LTS và kích hoạt cơ chế caching npm.
3. **Start Backend Server (SUT):** Cài đặt dependencies và khởi chạy backend `node server.js` ở chế độ background (`&`), sử dụng tiện ích `wait-on` để đảm bảo server `http://localhost:3000` đã sẵn sàng nhận kết nối trước khi chạy test.
4. **Execute Newman Tests:** Chạy toàn bộ bộ test suite Postman được tải lên folder `ci_tests` dưới dạng file `.csv` thông qua Newman CLI, kết hợp đọc biến môi trường từ file `hw06.postman_environment.json` và xuất báo cáo trực quan dưới dạng HTML.
5. **Upload Artifacts:** Đóng gói file báo cáo kiểm thử `newman-reports/report.html` và lưu trữ dưới dạng Build Artifact trên GitHub Actions (lưu trữ 14 ngày).

---

## 2. Kết quả chạy CI/CD

### 2.1. Kịch bản 1: Pipeline Run Thành Công Toàn Bộ 
* **Mục đích:** Kiểm tra tính ổn định của luồng CI/CD khi tất cả các assertion đều pass.
* **Mô tả commit:** `ci: add passing tests`
* **Kết quả:**
  * Toàn bộ các bước trong Job `Run Newman API Tests` hoàn thành với trạng thái **Passed (Xanh)**.
  * 100% assertion đạt trạng thái Success.
  * Artifact `newman-api-test-report` được sinh và tải lên thành công.

- Hình ảnh CI xanh: ![CI passing](ci_cd/pass.png)

### 2.2. Kịch bản 2: Pipeline Run Phát Hiện Test Case Thất Bại 
* **Mục đích:** Kiểm tra khả năng cảnh báo sớm của CI/CD khi phát hiện lỗi vi phạm nghiệp vụ hoặc hồi quy phần mềm.
* **Mô tả commit:** `ci: add failing tests`
* **Kết quả:**
  * Newman phát hiện assertion thất bại 
  * Newman ghi nhận kết quả Fail trên giao diện Console và đánh dấu cảnh báo trên summary của GitHub Actions.

- Hình ảnh CI đỏ: ![CI failing](ci_cd/fail.png)

---

## 3. Điểm hạn chế của cấu hình hiện tại

Do file yml được cấu hình để track toàn bộ file csv trong thư mục `ci_tests`, kết quả của ci có thể bị thay đổi (ví dụ: commit file failing trước sẽ khiến commit file passing bị fail). Để khắc phục, khi test xong, lập tức xoá file đó khỏi folder. Một cách khác là ta có thể quy định tên file được chấp nhận trong `ci_tests` để tránh CI track file không kiểm soát, tuy nhiên việc đặt một tên cố định có thể gây khó phân biệt giữa các bộ test trong một số trường hợp khi tên bộ test riêng, cụ thể sẽ giúp dev nhận ra bản chất của bộ test ngay.

---

## 4. Kết luận

Việc tích hợp bộ test Postman vào GitHub Actions giúp tự động hóa hoàn toàn quy trình kiểm thử API mỗi khi có thay đổi trong mã nguồn, đảm bảo tính toàn vẹn của hệ thống và ngăn ngừa lỗi hồi quy một cách liên tục.