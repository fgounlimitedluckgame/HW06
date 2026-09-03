# AI Critique

Trong bài tập này, em đã sử dụng AI để sinh ra các test case API, gợi ý biến môi trường, các pre/post request script cho test case, sinh file yml cho CI. Khi em sử dụng, em nhận ra những điều sau:

Điểm cộng: AI có thể generate những test case tương đối tốt, gợi ý cấu hình postman, gợi ý diagram và pseudocode cho quá trình sinh test case, và tạo cấu hình CI/CD, giúp thuận tiện cho việc làm bài tập

Điểm trừ: AI cũng có một số mặt hạn chế. Thứ nhất, các test case của AI sinh ra thường chỉ test những pattern phổ biến hoặc baseline, trong khi chưa đụng đến những trường hợp đặc biệt phải cần con người để tự thêm. Thứ hai, AI đã sinh ra các assertion scripts dưới dạng pseudocode khi sinh ra các state transition test đã được em đánh dấu `INCOMPLETE` (FR01: `FR01-ST-029` và `FR01-ST-030`. FR07: `FR07-ST-024` đến `FR07-ST-028`. FR15: `FR07-ST-024` đến `FR07-ST-027`), em đã chỉnh sửa lại bằng cách chỉ coi những assertion script dạng pseudocode như giả định lý thuyết, còn khi test thì sẽ dùng http code để kiểm thử. Ngoài ra, AI ban đầu chỉ sinh test case dưới dạng `markdown`, việc xuất các test case sang CSV phải qua bước trung gian, khá tốn thời gian.

Kết luận: Chỉ dùng AI để sinh template artifacts, nhưng human review vẫn là trên hết
