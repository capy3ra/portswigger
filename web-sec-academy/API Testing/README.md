![image](https://github.com/capy3ra/portswigger/assets/80744099/7ee56892-66bb-406d-a36f-406513ab4662)## API tesing

1. Exploiting a mass assignment vulnerability
- Thử tính năng như một user bt (đăng nhập -> chọn sản phẩm -> thêm vào giỏ hàng -> thanh toán)
- Quay lại proxy history xem nó có lộ api nào không
![image](https://github.com/capy3ra/portswigger/assets/80744099/e6cd7d73-5357-4737-94dd-363fa3b66d4b)

- Nhận thấy ở get API checkout có để lộ một vài param nghi ngờ. Đặc biệt là trường chọn discount
- Trong POST api checkout thêm trường chosen_discord với giá trị 100% -> Thành công.
![image](https://github.com/capy3ra/portswigger/assets/80744099/1d3573e7-896b-416c-913d-a6ef2bec060d)

2. Exploiting server-side parameter pollution in a query string
- Fuzz các tính năng trên web nhận thấy, ở chức năng quên mật khẩu khá đáng nghi khi mà request trả về một chuỗi json.
![image](https://github.com/capy3ra/portswigger/assets/80744099/9c72ff45-5317-455c-8bdb-93db8100ba4e)

- Thử các skill như chèn các character như &, # (encoding) để param pollution
- Khi chèn một param bất kỳ vào bằng & nhận thấy nó chèn thành công và hiện lên thông báo là param này không được hỗ trợ
![image](https://github.com/capy3ra/portswigger/assets/80744099/e5ab8b52-de85-4268-ae71-587545eca385)

- Khi chèn `#` vào thì nhận thấy hiện lên thông báo `Field not specified`. Có thể hiểu là khi chèn character `#` vào api server nó sẽ biến những phần sau thành fragment (Giống kiểu comment đi) nên phần định nghĩa param `field` bị mất và nó hiện lên thông báo lỗi như vậy. Như vậy xác định được trong internal api có một trường field 
![image](https://github.com/capy3ra/portswigger/assets/80744099/1c52cf5c-d614-4b63-b920-5494c37e1ef7)

- Craft trường field với các giá trị bất kỳ nhận được lỗi Invalid field. Khi thử với email, username thì nó hiện giá trị email, username của username truyền vào.
![image](https://github.com/capy3ra/portswigger/assets/80744099/d6436d4a-1027-465a-a371-6428c6ea8114)

- Trong phần forgotPassword.js nhận thấy nó đoạn redirect đến endpoint forgot-password với param reset_token
![image](https://github.com/capy3ra/portswigger/assets/80744099/fd018423-d493-4b21-8c03-622866dfcd3a)

- Truyền giá trị reset_token vào param field xem nó có hiện giá trị không.
![image](https://github.com/capy3ra/portswigger/assets/80744099/30bfc904-b9dc-4f99-88cd-6808c044f059)

- Tạo request quên mk với token vừa lấy được
- Thay đổi password -> Xóa user carlos

3. 
