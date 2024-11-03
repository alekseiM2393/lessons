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


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print()
h3 = House("ЖК Суворовский", 22)
h4 = House("ЖК Невский", 16)
h3.go_to(8)
print()
h4.go_to(20)
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
print(h1)
print(h2)
print(h3)
print(h4)


