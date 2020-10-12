class Mother:
    __name = ""

    def __init__(self, name):
        self.__name = name

    def name(self):
        return self.__name

    def print_inf(self):
        return f"Name: {self.name()}"

    def __str__(self):
        return self.print_inf()


class Daughter(Mother):
    __name = ""

    def __init__(self, name, mother):
        super().__init__(name)
        self.__name = mother

    def mother_name(self):
        return self.__name

    def print_inf(self):
        return f"Name: {self.name()} => Mother: {self.mother_name()}"


mother_name = Mother("Kate")
daughter_name = Daughter("Louisa", "Kate")

print(mother_name, daughter_name, sep='\n')