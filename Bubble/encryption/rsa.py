from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA


class rsa():
    def __init__(self):
        self.__rsa = RSA.generate(2048, Random.new().read)

    def genPrivateKey(self):
        return self.__rsa.exportKey()

    def genPublicKey(self):
        return self.__rsa.public_key().exportKey()

    @staticmethod
    def encrypt(msg, publicKey: str | bytes) -> bytes:
        key = RSA.importKey(publicKey)
        cipher = PKCS1_cipher.new(key)
        return cipher.encrypt(msg.encode())

    @staticmethod
    def decrypt(msg, privateKey: str | bytes) -> bytes:
        key = RSA.importKey(privateKey)
        cipher = PKCS1_cipher.new(key)
        return cipher.decrypt(msg, 0)

    def sign(self):
        pass

    def verify(self):
        pass


if __name__ == '__main__':
    a = rsa()
    pubKey = a.genPublicKey()
    priKey = a.genPrivateKey()
    b = a.encrypt(msg='wq', publicKey=pubKey)
    c = a.decrypt(b, priKey)
    print(c)
