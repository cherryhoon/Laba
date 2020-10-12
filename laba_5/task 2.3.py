class Animal:
    __name = ""
    __age = ""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def name(self):
        return self.__name

    def age(self):
        return self.__age

    def print_inf(self):
        return f"Name: {self.name()}; Age: {self.age()}"

    def __str__(self):
        return self.print_inf()


class Zebra(Animal):
    __hobby = 0

    def __init__(self, name, age, hobby):
        super().__init__(name, age)
        self.__hobby = hobby

    def print_inf(self):
        return f"Name: {self.name()}; Age: {self.age()}; Hobby: {self.__hobby}"

class Dolphin(Animal):
    __friends = 0

    def __init__(self, name, age, friends):
        super().__init__(name, age)
        self.__friends = friends

    def print_inf(self):
        return f"Name: {self.name()}; Age: {self.age()}; Friends: {self.__friends}"


z = Zebra("Martin", "17", hobby="running and eating")
d = Dolphin("Flipper", "9", friends="Martin and Robby")

print(z)
print(d)