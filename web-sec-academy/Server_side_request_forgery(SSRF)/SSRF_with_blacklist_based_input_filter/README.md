## SSRF with blacklist-based input filter

1. Ở lab này, đã được bổ sung thêm chức năng filter input dựa theo black_list để chống SSRF

![Img1](\asset/../img/error.png)

2. Thử thay url thành ``http://127.1/`` được.

![Img2](\asset/../img/bypass.png)

3. Truy cập admin panel với path ``/admin``

![Img3](\asset/../img/blocked.png)

4. ``admin`` cũng bị block. URL encode ``admin`` 

5. Nhận thấy phải double encode thì mới bypass được

![Img4](\asset/../img/bypass1.png)

6. Lấy url delete user ``carlos`` rồi double encode trước khi gửi.