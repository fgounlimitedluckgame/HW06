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

![200 instead of 201](bug_screenshots/200%20instead%20of%20201.png)
![200 part 2](bug_screenshots/200%20part%202.png)

---

## Bug 2: Nhảy quyền bằng cách thêm trường role trong payload đăng ký
- **Endpoint bị ảnh hưởng:** `POST /api/register`, 
- **Mô tả hành vi:** Khi đăng ký, người dùng có thể biến người đăng ký thành admin bằng cách thêm trường role trong payload
- **Cách thực hiện:** Tạo một body đăng ký, nhưng cuối payload thêm `"role": "admin"`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

![escalation 1](bug_screenshots/escalation%201.png)
![escalation 2](bug_screenshots/escalation%202.png)
![escalation 3](bug_screenshots/escalation%203.png)


---

## Bug 3: Lỗi schema validation
- **Endpoint bị ảnh hưởng:** `POST api/cart`, `api/products`
- **Mô tả hành vi:** Người dùng có thể thêm một trường không tồn tại vào body json và hệ thống vẫn chấp nhận
- **Cách thực hiện:** Tạo một body đăng ký, nhưng cuối payload thêm `"role": "admin"`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

![wrong schema 1](bug_screenshots/wrong%20schema%201.png)
![wrong schema 2](bug_screenshots/wrong%20schema%202.png)
![wrong schema 3](bug_screenshots/wrong%20schema%203.png)

---

## Bug 4: Body json rỗng được chấp nhận
- **Endpoint bị ảnh hưởng:** `/api/register`, `/api/cart`, `/api/products`
- **Mô tả hành vi:** Người dùng có thể dùng body json rỗng nhưng hệ thống vẫn chấp nhận
- **Cách thực hiện:** Dùng body `[]` hoặc `{}`
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

- **Minh hoạ issue trong test case đăng ký:**

![invalid json body 1](bug_screenshots/invalid%20JSON%20body.png)
![invalid json body 2](bug_screenshots/invalid%20JSON%202.png)
![invalid json body 3](bug_screenshots/invalid%20JSON%203.png)

--- 

## Bug 5: Lỗi xác thực bearer khiến cho người dùng thực hiện được quyền CRUD product bất chấp quyền
- **Endpoint bị ảnh hưởng:** `/api/products`
- **Mô tả hành vi:** Người dùng có thể không cần dùng authorization token hoặc token giả mà vẫn có thể thực hiện quyền CRUD của admin
- **Cách thực hiện:** Tạo một body tương tác với sản phẩm, nhưng thay thế bearer token thành `user token`, hoặc `null token`, hoặc một token giả
- **Kết quả mong đợi:** 403 Forbidden
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe


![invalid bearer](bug_screenshots/invalid%20bearer%20accepted.png)

---

## Bug 6: Body chứa lỗi nhập liệu được chấp nhận bởi hệ thống
- **Endpoint bị ảnh hưởng:** `/api/register`, `/api/cart`, `/api/products
- **Mô tả hành vi:** Người dùng có thể dùng body json rỗng nhưng hệ thống vẫn chấp nhận
- **Cách thực hiện:** Dùng body chứa các trường hợp lệ nhưng có lỗi nhập liệu như thiếu email, thiếu mật khẩu, thiếu tên, số lượng sản phẩm âm, số lượng sản phẩm có phần thập phân, dữ liệu chứa SQL Injection, lỗi IDOR, xml script,... 
- **Kết quả mong đợi:** 400 Bad Request
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

- **Hình ảnh minh hoạ về lỗi nhập liệu ở `/api/register:`**

![wrong input](bug_screenshots/wrong%20input.png)
![wrong input 2](bug_screenshots/wrong%20input%202.png)

---

## Bug 7: Email đăng ký bị trùng được chấp nhận
- **Endpoint bị ảnh hưởng:** `POST /api/register`
- **Mô tả hành vi:** Người dùng sử dụng body đăng ký chứa email đã được tạo trước đó vẫn có thể đăng ký tài khoản mới 
- **Cách thực hiện:** Tạo một register body chứa một email đã đăng ký trước đó (ví dụ có sẵn: `test@eshop.com`)
- **Kết quả mong đợi:** 409 Conflict
- **Kết quả thực tế:** 200 OK
- **Mức độ nghiêm trọng:** Severe

![duplicate email](bug_screenshots/duplicate%20email.png)
![duplicate email body](bug_screenshots/duplicate%20email%20body.png)




