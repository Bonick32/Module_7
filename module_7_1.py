class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        return file.read()

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_product_names = {line.split(', ')[0] for line in existing_products}

        # я конечно пришел к такому виду, как записал ниже, но стараюсь вникнуть и в короткую логичную запись
        # existing_product_names = set()
        #
        # for line in existing_products:
        #     name = line.split(', ')[0]
        #     existing_product_names.add(name)

        file = open(self.__file_name, 'a')
        for i in products:
            if i.name in existing_product_names:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file.write(f'{i} \n')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())