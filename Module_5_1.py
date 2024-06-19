class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует!')


H1 = House('Версаль', 25)
H2 = House('Спальник', 18)
H1.go_to(6)
H2.go_to(20)