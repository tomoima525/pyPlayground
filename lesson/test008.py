import test007

person = test007.Person(11, "Mary Jane")
print(person.name)


class Customer(test007.Person):
    def __init__(self, num, name, age):
        self.__age = age
        super().__init__(num, name)  # override consructor

    def get_age(self):
        return self.__age

    age = property(get_age) #set property

if __name__ == "__main__":
    c = Customer(5, "Luke Skywalker",25)
    print("{}:{}".format(c.name,c.age))
