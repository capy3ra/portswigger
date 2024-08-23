## Accidental exposure of private GraphQL fields

1. Scan introspection bằng InQL có được
![image](https://github.com/user-attachments/assets/46deaf18-dd29-44a4-a89d-e8204627f6ab)

2. Nhận thấy có query getUser có thể chứa Tk MK của user.
3. Gửi một request thể getUser id = 1

![image](https://github.com/user-attachments/assets/758a027e-f01e-4f18-830a-2635d0b2dc5b)

4. Lấy được account admin -> vào xóa user Carlos
