from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class aes():
    __key: bytes = None
    __iv: bytes = None
    __pendingMode: str = 'pkcs7'

    def __init__(self, key: bytes = None, iv: bytes = None):
        if key and iv:
            if len(key) % AES.block_size:
                self.__key = pad(data_to_pad=key, block_size=AES.block_size, style=self.__pendingMode)
            else:
                self.__key = key
            if len(iv) % AES.block_size:
                self.__iv = pad(data_to_pad=iv, block_size=AES.block_size, style=self.__pendingMode)
            else:
                self.__iv = iv

    def keyUpdate(self, key: bytes, iv: bytes):
        self.__dataAvailableCheck(key, iv)
        if len(key) % AES.block_size:
            self.__key = pad(data_to_pad=key, block_size=AES.block_size, style=self.__pendingMode)
        else:
            self.__key = key
        if len(iv) % AES.block_size:
            self.__iv = pad(data_to_pad=iv, block_size=AES.block_size, style=self.__pendingMode)
        else:
            self.__iv = iv

    def encrypt(self, msg: bytes) -> bytes:
        self.__dataAvailableCheck(self.__key, self.__iv)
        self.__dataAvailableCheck(self.__key, self.__iv)
        CBCAes = AES.new(self.__key, AES.MODE_CBC, self.__iv)
        return CBCAes.encrypt(
            pad(msg, block_size=AES.block_size, style=self.__pendingMode)
        )

    def decrypt(self, msg: bytes) -> bytes:
        self.__dataAvailableCheck(self.__key, self.__iv)
        self.__dataAvailableCheck(self.__key, self.__iv)
        CBCAes = AES.new(self.__key, AES.MODE_CBC, self.__iv)
        rawDecryptText = CBCAes.decrypt(msg)
        return unpad(rawDecryptText, block_size=AES.block_size, style=self.__pendingMode)

    @staticmethod
    def __dataAvailableCheck(key: bytes, iv: bytes):
        if key is None:
            raise ValueError()
        if iv is None:
            raise ValueError()


if __name__ == '__main__':
    print(AES.block_size)
    a = aes(b'12', b'22')
    b = a.encrypt(b'12')
    c = a.decrypt(bytes(b))
    print(b, c)
