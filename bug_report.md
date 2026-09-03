# Báo cáo lỗi trong kiểm thử API

**Số lỗi phát hiện:** 7

**Link github issues:** https://github.com/fgounlimitedluckgame/HW06/issues

---

## Bug 1: Response 200 OK thay vì 201 Created cho những test case tạo mới

- **Endpoint bị ảnh hưởng:** `POST /api/register`, `POST /api/cart`, `POST /api/products`
- **Mô tả hành vi:** 
Khi thực hiện một API request dạng tạo mới, khi request được thực hiện thành công, server sẽ trả về 200 OK thay vì 201 Created
- **Cách thực hiện:** Thực hiện đăng ký một tài khoản, hoặc thêm một đơn hàng, hoặc thêm một sản phẩm
- **Kết quả mong đợi:** 201 Created
- **Kết quả thực tế:** 200 OK

- **Mức độ nghiêm trọng:** Low, vì nó chỉ không đúng với tiêu chuẩn của HTML (lưu ý: test case dùng 200 OK thay vì 201 Created để tránh tạo false positive)

<img width="1399" height="466" alt="Image" src="https://github.com/user-attachments/assets/807a5ec5-9c43-4304-a6ba-1e78003c565f" />

<img width="1379" height="417" alt="Image" src="https://github.com/user-attachments/assets/f4caf13b-9aae-4d57-9511-4c8cca46406a" />

---

## Bug 2: Nhảy quyền bằng cách thêm trường role trong payload đăng ký
- **Endpoint bị ảnh hưởng:** `POST /api/register`, 
- **Mô tả hành vi:** Khi đăng ký, người dùng có thể biến người đăng ký thành admin bằng cách thêm trường role trong payload
- **Cách thực hiện:** Tạo một body đăng ký, nhưng cuối payload thêm `"role": "admin"`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

<img width="743" height="752" alt="Image" src="https://github.com/user-attachments/assets/e1509194-ad80-4948-bdac-875b1cb81a54" />

<img width="752" height="735" alt="Image" src="https://github.com/user-attachments/assets/3d549b97-360f-4bbc-bc71-452aed9f4680" />

<img width="762" height="762" alt="Image" src="https://github.com/user-attachments/assets/745004fd-73c2-4780-b92c-71fc014ed7f6" />

---

## Bug 3: Lỗi schema validation
- **Endpoint bị ảnh hưởng:** `POST api/cart`, `api/products`
- **Mô tả hành vi:** Người dùng có thể thêm một trường không tồn tại vào body json và hệ thống vẫn chấp nhận
- **Cách thực hiện:** Tạo một body đăng ký, nhưng cuối payload thêm `"role": "admin"`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

<img width="743" height="752" alt="Image" src="https://github.com/user-attachments/assets/e1509194-ad80-4948-bdac-875b1cb81a54" />

<img width="752" height="735" alt="Image" src="https://github.com/user-attachments/assets/3d549b97-360f-4bbc-bc71-452aed9f4680" />

<img width="762" height="762" alt="Image" src="https://github.com/user-attachments/assets/745004fd-73c2-4780-b92c-71fc014ed7f6" />

---

## Bug 4: Body json rỗng được chấp nhận
- **Endpoint bị ảnh hưởng:** `/api/register`, `/api/cart`, `/api/products`
- **Mô tả hành vi:** Người dùng có thể dùng body json rỗng nhưng hệ thống vẫn chấp nhận
- **Cách thực hiện:** Dùng body `[]` hoặc `{}`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

- **Minh hoạ issue trong test case đăng ký:**

<img width="745" height="715" alt="Image" src="https://github.com/user-attachments/assets/319001b8-5c55-403d-9d32-c6dfa82c3df2" />
<img width="731" height="730" alt="Image" src="https://github.com/user-attachments/assets/52932bbc-e7a1-46d4-a21d-cb743ea4529a" />
<img width="760" height="757" alt="Image" src="https://github.com/user-attachments/assets/7817c1b6-5bbe-4f35-9422-99dec868c269" />

--- 

## Bug 5: Lỗi xác thực bearer khiến cho người dùng thực hiện được quyền CRUD product bất chấp quyền
- **Endpoint bị ảnh hưởng:** `/api/products`
- **Mô tả hành vi:** Người dùng có thể không cần dùng authorization token hoặc token giả mà vẫn có thể thực hiện quyền CRUD của admin
- **Cách thực hiện:** Tạo một body tương tác với sản phẩm, nhưng thay thế bearer token thành `user token`, hoặc `null token`, hoặc một token giả
- **Kết quả mong đợi:** 403 Forbidden
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe


<img width="1435" height="955" alt="Image" src="https://github.com/user-attachments/assets/2386bcd1-945c-488c-878b-87b9bd375871" />

---

## Bug 6: Body chứa lỗi nhập liệu được chấp nhận bởi hệ thống
- **Endpoint bị ảnh hưởng:** `/api/register`, `/api/cart`, `/api/products
- **Mô tả hành vi:** Người dùng có thể dùng body json rỗng nhưng hệ thống vẫn chấp nhận
- **Cách thực hiện:** Dùng body chứa các trường hợp lệ nhưng có lỗi nhập liệu như thiếu email, thiếu mật khẩu, thiếu tên, số lượng sản phẩm âm, số lượng sản phẩm có phần thập phân, dữ liệu chứa SQL Injection, lỗi IDOR, xml script,... 
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

- **Hình ảnh minh hoạ về lỗi nhập liệu ở `/api/register:`**

<img width="1447" height="950" alt="Image" src="https://github.com/user-attachments/assets/e634a9af-5342-414e-884b-a177a9b8a24d" />
<img width="1391" height="353" alt="Image" src="https://github.com/user-attachments/assets/d147c7a3-8991-4bc6-801c-c8f81e621e4e" />

---

## Bug 7: Email đăng ký bị trùng được chấp nhận
- **Endpoint bị ảnh hưởng:** `POST /api/register`
- **Mô tả hành vi:** Người dùng sử dụng body đăng ký chứa email đã được tạo trước đó vẫn có thể đăng ký tài khoản mới 
- **Cách thực hiện:** Tạo một register body chứa một email đã đăng ký trước đó (ví dụ có sẵn: `test@eshop.com`)
- **Kết quả mong đợi:** 409 Conflict
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

<img width="1346" height="825" alt="Image" src="https://github.com/user-attachments/assets/99e7c9ca-ec72-4cf3-8e29-e43485d11839" />
<img width="1360" height="414" alt="Image" src="https://github.com/user-attachments/assets/805c42da-29a2-45a0-a5ea-bff2ee5043ec" />




