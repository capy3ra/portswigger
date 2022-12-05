import base64
import hashlib

fr = open("password.txt",'r')
fw = open("cookie.txt", 'a')
for i in fr:
    message = "carlos:"
    i = i[:-1]
    md5 = hashlib.md5(i.encode())
    newi = md5.hexdigest()
    message += newi
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    fw.write(base64_message + "\n")
    # print(base64.b64encode(('wiener:' + hashlib.md5(i.encode()).hexdigest()).encode()))