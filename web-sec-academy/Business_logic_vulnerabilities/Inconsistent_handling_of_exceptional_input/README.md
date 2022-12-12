## Inconsistent handling of exceptional input

1. Nhận thấy chỉ những người dùng có email ``@dontwannacry`` mới có quyền admin

2. Thử đăng ký với email có độ dài rất lớn thì nhận thấy vẫn nhận được email xác thực.

![Img1](\asset/../img/test.png)

3. Nhưng email sau khi đăng nhập thì chỉ còn 255 ký tự đầu.

![Img2](\asset/../img/email_length.png)

4. Từ đó ta có thể thêm payload với phần trước @ trong email đủ dài để email sau khi đăng ký chỉ còn phần subdomain ``@dontwannacry``

![Img3](\asset/../img/done.png)

5. Vào admin panel xóa tài khoản carlos