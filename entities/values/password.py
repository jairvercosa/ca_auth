

class Password:

    def __init__(self, value):
        self.__value = value

    def __bool__(self):
        return bool(self.__value)

    def __eq__(self, value):
        return self.__value == value
