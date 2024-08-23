## Accessing private GraphQL posts

1. Bắt proxy request call api. Request retrive tất cả các post
2. Vào một post bất kỳ nhận được có một api với 1 param id được cung cấp
3. Dùng InQL trong burp extension để lấy được schema của các field -> Nhận thấy có trường postPassword -> Thêm trường vào khai báo request

 
