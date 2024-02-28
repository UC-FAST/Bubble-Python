import socket
import time

while True:
    obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    obj.bind(('127.0.0.1', 12345))
    obj.connect(("127.0.0.1", 8080))
    obj.send(b'121')
    ret = str(obj.recv(1024),encoding="utf-8")
    print(ret)
    obj.close()
    time.sleep(1)