import os


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if not os.path.isfile(self.__file_name):
            return 'NO FILE'
        file = open(self.__file_name, 'r+', encoding='utf-8')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        for product in products:
            if isinstance(product, Product):
                print(self.write_to_file(product))

    def write_to_file(self, data):
        file = open(self.__file_name, 'a')
        if self.get_products():
            if data.name not in self.get_products():
                file.write(Product(data.name, data.weight, data.category).__str__() + '\n')
                file.close()
                return data.name + ' was added to the shop!'
            else:
                file.close()
                return data.name + ' is already in the shop'
        else:
            file.write(Product(data.name, data.weight, data.category).__str__() + '\n')
            file.close()
            return data.name + ' was added to the shop!'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
