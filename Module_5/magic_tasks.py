from class_attributes import House


class House2(House):
    def __len__(self):
        return self.floor_numbers

    def __str__(self):
        return str(f"Название: {self.name}, кол-во этажей: {self.floor_numbers}")


if __name__ == '__main__':
    def print_house():
        h1 = House2('ЖК Эльбрус', 10)
        h2 = House2('ЖК Акация', 20)

        # __str__
        print(h1)
        print(h2)

        # __len__
        print(len(h1))
        print(len(h2))


    print_house()
