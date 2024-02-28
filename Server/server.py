import socket






if __name__=='__main__':
    pass
s=socket.socket()

s.bind(('127.0.0.1',8080))
s.listen()
while True:
    cs=s.accept()
    print(cs)
    cs[0].send(b'sa')
    cs[0].close()