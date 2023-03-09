## Internal cache poisoning

1. Dùng tool Param Miner xác định được ``X-Forwarded-Host`` là một unkeyed param.

![Img1](\asset/../img/unkeyed_param.png)

2. Với một host bất kỳ nhận thấy nó sẽ được gán thêm vào trước link import js file. Để `X-Forwarded-Host` là trang exploit rồi craft trang exploit thành path sau khi inject

![Img2](\asset/../img/done.png)