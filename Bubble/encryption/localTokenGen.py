from hashlib import md5


class localTokenGen():
    def __init__(self, seed: str = '0'):
        self.__seed = seed
        self.__last = seed

    def next(self, length=16):
        result = self.__algorithm()
        self.__last = result
        if length:
            return result[:length]
        return result

    def __algorithm(self):
        hashGen = md5()
        hashGen.update(self.__last.encode())
        return hashGen.hexdigest()
