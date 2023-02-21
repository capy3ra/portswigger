## Server-side template injection with information disclosure via user-supplied objects (REFER)

1. Phát hiện được lab sử dụng django template khi fuzz

![Img1](\asset/../img/detect.png)

2. Gọi đến build-in debug để xem từ template có thể truy xuất đến những object nào

![Img2](\asset/../img/list_object.png)

3. Trong đó `settings` object chứa trường `secret-key`. Goij đến đó để lấy key ->submit

![Img3](\asset/../img/done.png)