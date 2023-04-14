## Detecting server-side prototype pollution without polluted property reflection

1. Trong burp repeater, modify nhằm để request bị sai syntax nhận thấy có key "error".

![image](https://user-images.githubusercontent.com/80744099/231970870-f14066ba-add8-45c2-9729-9c03bcdde286.png)

2. Thêm key "error" với status code khác ở json trong request thành 
```
"error":{"statusCode":200}
```

3. Thì nhận thấy ta có thẻ override thành công status code

![image](https://user-images.githubusercontent.com/80744099/231971574-87397dae-0d31-44a1-a829-86201543d2c9.png)
