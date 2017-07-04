# coding:utf-8
import socket
T1="""HTTP/1.1 200 OK\r\n\r\n
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Null</title>
</head>
<body>
"""

T2="""
</body>
</html>
"""

def handle_request(client):
    buf = client.recv(1024)
    print buf
    T3=str(buf).replace('\n','<br />')
    client.send(T1+T3+T2)
    #client.send("Hello, World")


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
