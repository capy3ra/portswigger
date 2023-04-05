## Response queue poisoning via H2.TE request smuggling

1. Từ đề bài ta có thể nhận định đây là H2.TE request smuggling. 

![image](https://user-images.githubusercontent.com/80744099/230023619-8cf5f092-8305-4099-a654-ccf5741c0cd2.png)

2. Để tiến hành đầu độc hàng đợi response. Ta sẽ lợi dụng H2.TE request smuggling để khi gửi request sau. Phía FE coi như 1 request nhưng BE lại split nó thành 2 request trỏ tới 2 endpoint không tồn tại để generate và lưu trữ 2 response Not Found trong response queue. 

![image](https://user-images.githubusercontent.com/80744099/230025552-c99dd921-d4b0-42ce-9f98-a21397528677.png)
![image](https://user-images.githubusercontent.com/80744099/230025575-a019f695-5632-4586-9ade-df89b900bf8e.png)

3. Gửi request liên tục đến khi bắt được request của admin.

![image](https://user-images.githubusercontent.com/80744099/230025806-7676e81b-7f39-4cae-9b2b-26c2974f5e3a.png)

4. Thay giá trị cookie của admin rồi vào admin panel xóa user carlos 

![image](https://user-images.githubusercontent.com/80744099/230026130-9e8a5962-018f-47d7-bc13-80845146cb7c.png)
