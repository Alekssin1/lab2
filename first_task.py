class Product:

    def __init__(self, price, brand, description, **product_dimensions):
        self.price = price
        self.brand = brand
        self.description = description
        self.product_dimensions = product_dimensions

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError("U must enter a number > 0")
        self.__price = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise TypeError("Brand must be a string")
        self.__brand = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        self.__description = value

    @property
    def product_dimensions(self):
        return self.__product_dimensions

    @product_dimensions.setter
    def product_dimensions(self, value):
        if not isinstance(value, dict) or not value:
            raise TypeError("Product dimensions must be a dict")
        self.__product_dimensions = value

    def __str__(self):
        return '\nProduct data:\nPrice: ' + str(
            self.price) + ' UAH\nBrand: ' + self.brand + '\nDescription: ' + self.description + '\nDimension: ' \
               + ', '.join(list(map(str, list(self.product_dimensions.values())))) + '\n'


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self.__name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError("Patronymic must be a string")
        self.__patronymic = value

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        if not len(value) == 10 or not isinstance(value, str):
            raise ValueError('Incorrect input, mobile phone should be like 0973334444')
        self.__mobile_phone = value

    def __str__(self):
        return '\nCustomer data:\nSurname: ' + self.surname + '\nName: ' + self.name + '\nPatronymic: ' \
               + self.patronymic + '\nMobile phone: ' + self.mobile_phone + '\n'


class Order:

    def __init__(self, customer, **products):
        self.customer = customer
        self.products = products
        self.total_price = 0

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        if not value:
            raise TypeError("There must be at least one customer")
        self.__customer = value

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        if not isinstance(value, dict) or not value:
            raise TypeError("Products must be a dict")
        self.__products = value

    def get_total(self):
        for key in self.products:
            self.total_price += self.products[key].price
        return '\nTotal price: ' + str(round(self.total_price, 2))

    def customer_data(self):
        return self.customer

    def product_data(self):
        return '\n'.join(list(map(str, list(self.products.values()))))


jeans = Product(4900.00, "Levi's", "blue slim fit jeans", length=70, width=50, height=20)
hoodie = Product(5399.99, "Levi's", "Casual hoodie for everyday", length=70, width=50, height=20)
sneakers = Product(7777.77, "Nike", "Jordan is the best sneakers for basketball", length=38, width=30, height=15)
client = Customer('Dzhulai', 'Anthony', 'Peterson', '0965443211')
order = Order(client, first_product=jeans, second_product=hoodie, third_product=sneakers)
print(order.product_data(), order.customer_data(), order.get_total())
