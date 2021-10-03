class Product:

    def __init__(self, price, brand, description, **product_dimensions):
        if not isinstance(price, (int, float)):
            raise TypeError("U must enter a number")
        self.price = price
        self.brand = brand
        self.description = description
        self.product_dimensions = product_dimensions

    def get_price(self):
        return self.price

    def __str__(self):
        return '\nProduct data:\nPrice: ' + str(
            self.price) + ' UAH\nBrand: ' + self.brand + '\nDescription: ' + self.description + '\nDimension: ' \
               + ', '.join(list(map(str, list(self.product_dimensions.values())))) + '\n'


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        if not len(mobile_phone) == 10:
            raise ValueError('Incorrect input, mobile phone should be like 0973334444')
        self.mobile_phone = mobile_phone

    def __str__(self):
        return '\nCustomer data:\nSurname: ' + self.surname + '\nName: ' + self.name + '\nPatronymic: ' \
               + self.patronymic + '\nMobile phone: ' + self.mobile_phone + '\n'


class Order:

    def __init__(self, customer, **products):
        self.client = customer
        self.products = products
        self.total_price = 0

    def get_total(self):
        for key in self.products:
            self.total_price += self.products[key].get_price()
        return '\nTotal price: ' + str(self.total_price)

    def customer_data(self):
        return self.client

    def product_data(self):
        return '\n'.join(list(map(str, list(self.products.values()))))


jeans = Product(4900.00, "Levi's", "blue slim fit jeans", length=70, width=50, height=20)
cs = Product(5399.99, "Levi's", "Casual hoodie for everyday", length=70, width=50, height=20)
client = Customer('Dzhulai', 'Anthony', 'Peterson', '0965443211')
order = Order(client, first_product=jeans, second_product=cs)
print(order.product_data(), order.customer_data(), order.get_total())
