import base64
from hashlib import md5


class msgTrans:
    def __init__(self, msg):
        self.__msg = msg

    def base64Encode(self):
        return msgTrans(base64.b64encode(bytes(self)))

    def base64Decode(self):
        return msgTrans(base64.b64decode(bytes(self)))

    def md5(self):
        md5Hash = md5()
        md5Hash.update(bytes(self))
        return msgTrans(md5Hash.hexdigest())

    def __str__(self):
        if isinstance(self.__msg, bytes):
            try:
                return self.__msg.decode()
            except UnicodeError:
                return str(self.__msg)
        else:
            return str(self.__msg)

    def __bytes__(self):
        if not isinstance(self.__msg, bytes):
            return bytes(self.__msg, 'UTF8')
        else:
            return self.__msg

    def __repr__(self):
        return self.__msg

    def __len__(self):
        return len(self.__msg)


if __name__ == '__main__':
    a = msgTrans(b'12')
    print(a)
    print(a.base64Encode().__repr__())
