class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        elif isinstance(new_floor, int):
            list_ = []
            for i in range(1, new_floor + 1):
                list_.append(i)
            print(*list_)


House1 = House('ЖК Высота', 24)
House2 = House('ЖК Южный Бульвар', 10)
House1.go_to(20)
House2.go_to(5)
House1.go_to(0)
House2.go_to(15)