## Basic SSRF against the local server

1. Nhận thấy trong chức năng check stock, sẽ tạo 1 request với param ``stockApi`` có giá trị trỏ đến 1 url để lấy dữ liệu.

2. Đổi lại giá trị của ``stockApi`` thành ``http://localhost/admin`` để fetch dữ liệu trang admin

![Img1](\asset/../img/admin_page.png)

3. Thay url bằng url để xóa ``carlos`` user.

![Img2](\asset/../img/done.png)