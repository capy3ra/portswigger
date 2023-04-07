## CL.0 request smuggling

1. Khi ta click vào trang admin panel thì nhận được message ``Path /admin is blocked`` 

2. Ở đề bài, có gợi ý ta rằng ở BE server ignores CL header trong request tới một vài endpoint. Tức là với các request này phần body mặc định có CL là 0.

3. Để xác định endpoint này, craft request kèm 1 request smuggling trỏ tới một endpoint không tồn tại để khi mà thành công thì response trả về code 404. Thử với các endpoint trong proxy log. 

![image](https://user-images.githubusercontent.com/80744099/230570731-ba3e5f4d-7b61-4560-8801-5c640bbc008f.png)

4. Nhận thấy các endpoint tới file ảnh đều ignore CL header. Khi gửi request thứ 2 thì smuggling request sẽ có dạng như sau để nó trả về 404
```
GET /example HTTP/1.1
X-Ignore: xPOST /resources/images/blog.svg HTTP/2
Host: 0abd002f04a74d4a80f6949b001200cc.web-security-academy.net
...
```

5. Đổi path của smuggling request thành admin thì thấy bypass thành công do request này đã nằm sẵn trong backend. -> xóa user carlos

![image](https://user-images.githubusercontent.com/80744099/230570618-b83eb6e6-c13d-439c-ad3a-44f8e890cacd.png)
