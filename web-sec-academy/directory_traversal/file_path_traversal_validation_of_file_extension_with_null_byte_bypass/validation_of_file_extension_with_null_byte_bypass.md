## File path traversal, validation of file extension with null byte bypass

1. Theo đề bài, lab có lỗ hổng directory traversal trong url ảnh của product. Tuy nhiên ở lab này, server sẽ tiến validate path xem phần mở rộng của file có đúng như mong đợi không. 

2. Sử dụng ``null`` byte để bypass lab này. Payload:
- ```/../../../etc/passwd%00.jpg```  (với ``%00`` là decode của ``null``)

![Img1](\asset/../done.png)