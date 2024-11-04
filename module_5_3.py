class House:

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print("Такого этажа не существует!")

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f"название: {self.name} колличество этажей {self.number_of_floor}")

    def __eq__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor == other.number_of_floor

    def __gt__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor >= other.number_of_floor

    def __lt__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor <= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other,(int,House)):
            return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floor + value)

    def __iadd__(self, value):
            return self.__add__(value)

    def __radd__(self, value):
            return self.__add__(value)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)


print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# False
# Название: ЖК Эльбрус, кол-во этажей: 20
# True
# Название: ЖК Эльбрус, кол-во этажей: 30
# Название: ЖК Акация, кол-во этажей: 30
# False
# True
# False
# True
# False