## API tesing

1. Exploiting a mass assignment vulnerability
- Thử tính năng như một user bt (đăng nhập -> chọn sản phẩm -> thêm vào giỏ hàng -> thanh toán)
- Quay lại proxy history xem nó có lộ api nào không
![image](https://github.com/capy3ra/portswigger/assets/80744099/e6cd7d73-5357-4737-94dd-363fa3b66d4b)

- Nhận thấy ở get API checkout có để lộ một vài param nghi ngờ. Đặc biệt là trường chọn discount
- Trong POST api checkout thêm trường chosen_discord với giá trị 100% -> Thành công.
![image](https://github.com/capy3ra/portswigger/assets/80744099/1d3573e7-896b-416c-913d-a6ef2bec060d)

2. 
