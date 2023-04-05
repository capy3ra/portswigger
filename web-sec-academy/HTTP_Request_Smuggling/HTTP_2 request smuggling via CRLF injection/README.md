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

6. Giờ chúng ta tạo một 
