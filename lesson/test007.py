# Handle class
class Person:
    def __init__(self, num, name):
        self.__num = num  #Capsule variables
        self.__name = name

    def set_num(self, num):
        self.__num += num

    def get_name(self):
        return self.__name
    def get_num(self):
        return self.__num


    def no_method(self):
        pass

    num = property(get_num, set_num)
    name = property(get_name)

if __name__ == "__main__":
    taro = Person(1, "John Doe")
    print("{}:{}".format(taro.num, taro.name))
    taro.set_num(10)
    print(taro.num)
