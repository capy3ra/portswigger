## HTTP/2 request smuggling via CRLF injection

1. Nhận thấy ở chức năng search sẽ ghi lại lịch sử tìm kiếm ứng với từng cookie.

2. Khi gửi POST request truy vấn một giá trị search mà không kèm giá trị session cookie thì nhận được một cookie mới.

![image](https://user-images.githubusercontent.com/80744099/229977014-aa274257-7902-4167-ab99-174488f05bfd.png)

3. Thử CRLF injection vào header của request.
```
Name: foo
Value: bar\r\nContent-Length:10
```

![image](https://user-images.githubusercontent.com/80744099/229977608-971db346-fb46-4d7c-b603-55d71d483876.png)

4. Với thông báo trùng header CL như vậy tức là chèn thành công. Thử với TE
```
Name: foo
Value: bar\r\nTranfer-Encoding: chunked
```

5. Khi gửi request thứ 2 nhận được lỗi not found do sau khi request thứ nhất bị cắt ở ký tự `0` phần còn lại sẽ đượ thêm vào requets sau làm cho nó có dạng
```
PayloadPOST / HTTP/2
HOST: ...
```

![image](https://user-images.githubusercontent.com/80744099/229980359-a79238e2-c58c-448d-a969-007415b5874c.png)

6. Giờ chúng ta tạo một POST / request với truy vấn search rồi đợi victim truy cập vào host khi đó request của victim sẽ được reflect lên lịch sử search của attacker.

![image](https://user-images.githubusercontent.com/80744099/229982992-b1c50ac9-ca61-4ad2-954a-d25fa8bd4098.png)

7. Nhận được request từ victim có chứa session cookie -> Thay đổi giá trị cookie hiện tại thành của victim rồi để truy cập tài khoản carlos

![image](https://user-images.githubusercontent.com/80744099/229982753-8593f833-6c91-4bcf-be25-c37a97389366.png)
