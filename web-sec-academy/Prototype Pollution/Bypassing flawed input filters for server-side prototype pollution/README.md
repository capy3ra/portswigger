## Bypassing flawed input filters for server-side prototype pollution

1. Thử chức năng update thông tin tài khoản người dùng, để override status code bằng magic method ``__proto__`` mà không thành công

![image](https://user-images.githubusercontent.com/80744099/231984660-b03198ca-11dd-41ba-8f54-e438df05c91e.png)

![image](https://user-images.githubusercontent.com/80744099/231984729-d73e4e05-91be-47a1-ad0a-c596e1713d57.png)

2. Quay qua sử dụng method có sẵn `constructor` trong object. 

![image](https://user-images.githubusercontent.com/80744099/231985237-1a908e68-8389-4111-8919-7c4524c6ceab.png)
 
![image](https://user-images.githubusercontent.com/80744099/231985290-af5af743-b604-4e53-843d-6f6ffcd6fc22.png)

3. Nhận thấy ghi đè thành công 

4. Chèn thuộc tính ``"isAdmin":true`` thông qua constructor nhận thấy leo quyền thành công

![image](https://user-images.githubusercontent.com/80744099/231986129-cb87793b-f1f8-44d1-941c-d4626f6f5018.png)

5. Vào admin panel xóa user carlos

