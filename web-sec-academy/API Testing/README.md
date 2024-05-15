![image](https://github.com/capy3ra/portswigger/assets/80744099/0b29ee79-9b4b-4f85-ae3b-f97a269e785c)![image](https://github.com/capy3ra/portswigger/assets/80744099/7ee56892-66bb-406d-a36f-406513ab4662)## API tesing

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

3. Exploiting server-side parameter pollution in a REST URL
- Trong chức năng quên mật khẩu khi nhập username nó trả về file json khá đáng nghi với những xử lý API
![image](https://github.com/capy3ra/portswigger/assets/80744099/4f6179cd-1ed4-4c02-a0d0-c307d056690c)

- Khi thử fuzz với `&` đã encode nhận thấy nó được giải mã luôn và thêm vào username
![image](https://github.com/capy3ra/portswigger/assets/80744099/56dacb97-f3ec-4a37-98e9-78aba8d7f6cf)

- Còn khi fuzz với `#` đã encode nhận thấy có vẻ nó đã truncate 1 đoạn và hiện lên thông báo lỗi `invalid route`.
- Khi thử với `administrator/../admin` nhận thấy chỉ nhận octet cuối.
![image](https://github.com/capy3ra/portswigger/assets/80744099/99d5f36f-c239-46da-8aba-f1ef5b2a93b3)

- Thử tiếp với các đoạn path traversal mới. Nhận được thông báo URL not found.
![image](https://github.com/capy3ra/portswigger/assets/80744099/262c86e1-11ad-4193-ae57-0fd2217a716f)

- Có thể đoán là api này lưu theo kiểu thư mục. `cd ..` hơi quá nên không quá thư mục có sẵn. Còn những đoạn trước lỗi vì nó không trỏ được vào file nào.
- Với gợi ý là các api definition. Thử đoạn file openapi.json (sử dụng đồng thời # để truncation đoạn sau)
![image](https://github.com/capy3ra/portswigger/assets/80744099/e71963a0-7590-4a09-93ad-41f31b2e1c68)

- Ở đây có hướng dẫn đoạn API search trường theo user:
`/api/internal/v1/users/{username}/field/{field}`
- Ở đây ta biết có một field là email.
- Đọc file forgotPassword.js biết được có một field là `passwordResetToken`
![image](https://github.com/capy3ra/portswigger/assets/80744099/22567648-52b9-49f4-ae97-527d05ffa585)

- Đây chính là giá trị của param reset-token.
![image](https://github.com/capy3ra/portswigger/assets/80744099/d5443e51-6cb5-437f-afcf-8e51bbb6150d)

- Truy cập vào endpoint đó để đổi password
