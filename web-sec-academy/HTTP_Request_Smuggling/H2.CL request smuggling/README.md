## H2.CL request smuggling

1. Theo đề bài ta được biết máy chủ front-end của lab sẽ downgrades HTTP/2 requests về HTTP/1 để back-end server có thể xử lý.

2. Gửi vào repeater POST / request thêm header `Content-Length` thử gửi một vài payload chuẩn thì không có vấn đề gì

![image](https://user-images.githubusercontent.com/80744099/229679852-23adccba-5d3c-41b5-9b3b-d444116c1170.png)

3. Nhưng khi giảm bớt giá trị `Content-Length` đi 1 giá trị thì trong request thứ 2 gửi đi nhận được 404 status code (HTTP/2, uncheck Update Content-Length)

![image](https://user-images.githubusercontent.com/80744099/229680207-e3181718-21e0-4343-9cf6-cf4570502538.png)

4. Có thể do khi cắt bớt body trong request làm cho request thứ 2 được gán thêm phần còn dư trong request thứ 1 làm nó có dạng
```
tPOST / HTTP/2
Host: 0aec002f03191cb880e20888005000a9.web-security-academy.net
...
```

5. Từ đó dẫn đến lỗi 404, điều đó chứng tỏ khi downgrades mà http/2 có sẵn header `Content-Length`  thì HTTP/1 cũng sẽ lấy luôn giá trị đó.

6. Nhận thấy khi thêm với request tới path `/resources` sẽ trả về một 302 code redirect tới trang với từng endpoint. 

![image](https://user-images.githubusercontent.com/80744099/229682892-e3f1e607-be38-426b-b2ea-97bb11eb546e.png)

7. Nơi có thể khai thác để nó redirect đến endpoint attacker kiếm soát.

![image](https://user-images.githubusercontent.com/80744099/229683014-e36fc502-44e9-48b9-8f29-23210916f1d5.png)

8. Craft trang exxploit

![image](https://user-images.githubusercontent.com/80744099/229683260-8706ade3-e340-46cd-ad01-5ea6d047b70f.png)

9. Thay đổi gái trị cua host trong http reqeuts smuggling.

![image](https://user-images.githubusercontent.com/80744099/229684712-b0d6f731-7c97-4dd4-bea0-72ea186164f9.png)
