## Web cache poisoning via ambiguous requests

1. Thêm một header `Host` nữa rồi đợi cache hết hạn gửi request nhận thấy giá trị `Host` thứ 2 ghi đè lên `Host` 1 để rồi nó được reflect trên response.

![Img1](\asset/../img/duplicate_header.png)

2. Inject payload `test.com"></script><script>alert(document.cookie)</script>`

![Img2](\asset/../img/done.png)