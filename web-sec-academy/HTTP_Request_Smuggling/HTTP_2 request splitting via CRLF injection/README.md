## HTTP/2 request splitting via CRLF injection

1.  Lab gợi ý có vul response queue poisoning. Tiến hành split 1 request thành 2 request ở phía Backend rồi lưu vào response queue bằng CRLF injection HTTP/2 header.
```
Name: foo
Value: 
bar

GET /test HTTP/1.1
Host: 0afd008703d2a52a8141071a00d600f4.web-security-academy.net
```

2. Như vậy sau khi vượt qua phía FE server. Ở phía BE, sẽ được chia làm 2 request với điểm cắt là ``/r/n/r/n`` rồi lưu request sau vào queuee. Ta trỏ cả 2 request tới endpoint không tồn tại để response trả về là 404 not found để phân biệt với response của victim. 

![image](https://user-images.githubusercontent.com/80744099/230158986-71975502-a906-4956-af50-03a957720f85.png)

3. Sau khi gửi request chờ 10s để victim truy cập vào trang admin khi đó victim sẽ nhận được response của request được tách ra từ request ban đầu và đẩy response của victim vào queue. 

![image](https://user-images.githubusercontent.com/80744099/230159040-106ba6d3-45bd-4273-ac2d-805a0ff62de1.png)

4. Đổi lấy giá trị cookie của admin rồi xóa user carlos
