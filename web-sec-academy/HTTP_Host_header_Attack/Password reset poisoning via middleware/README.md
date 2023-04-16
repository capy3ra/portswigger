## Password reset poisoning via middleware

1. Dùng thử chức năng để reset mật khẩu

2. Trong request POST /forgot-password dùng kỹ thuật bypass bằng x-forwarded-host header để trỏ đến domain do ta kiểm soát

![image](https://user-images.githubusercontent.com/80744099/232332562-e0347623-34dd-4903-b49e-12168f5d392e.png)

3. Trong access log nhận thấy request GET /forgot-password với `temp-forgot-password-token` được gửi tới exploit server.

![image](https://user-images.githubusercontent.com/80744099/232332614-1cda991f-fefa-442b-bbda-f058f027b564.png)

4. Truy cập endpoint để đổi pass cho user carlos
