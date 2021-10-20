import json


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """ Insert value to the tree."""
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_root(value, self.root)

    def insert_root(self, value, current_root):
        """ inserts a value at a specific root (left or right)
            (sorting tree by code)
        """
        if list(value.keys())[0] < list(current_root.value.keys())[0]:
            if current_root.left is None:
                current_root.left = Node(value)
            else:
                self.insert_root(value, current_root.left)

        elif list(value.keys())[0] > list(current_root.value.keys())[0]:
            if current_root.right is None:
                current_root.right = Node(value)
            else:
                self.insert_root(value, current_root.right)

    def search(self, value):
        """ Find the element in tree and return it """
        if not self.root:
            return False
        return self.search_root(value, self.root)

    def search_root(self, value, current_root):
        if value == list(current_root.value.keys())[0]:
            return current_root.value
        elif value < list(current_root.value.keys())[0] and current_root.left:
            return self.search_root(value, current_root.left)
        elif value > list(current_root.value.keys())[0] and current_root.right:
            return self.search_root(value, current_root.right)
        else:
            return False


class BinaryTree:
    tree = Tree()

    def __init__(self, code, price):
        if not (isinstance(code, int) and isinstance(price, (int, float))):
            raise TypeError("Code and price must be an integers")
        BinaryTree.tree.insert({code: price})

    @classmethod
    def cost_of_products(cls, code, quantity):
        """ Calculates the value of a certain product in a certain amount and return it"""
        print(cls.tree.search(code))
        return quantity * cls.tree.search(code)[code]


with open("product_info.json") as f:
    for element in json.load(f):
        BinaryTree(int(list(element.keys())[0]), int(element[list(element.keys())[0]]))
try:
    number_of_products = int(input('Number of products: '))
    print("1<=Code<=14")
    total_cost = 0
    for i in range(number_of_products):
        code = int(input('Enter code of product: '))
        if code < 1 or code > 14:
            raise TypeError("Code must be more than 0 and less than 15")
        quantity = (int(input('Enter number of current product: ')))
        total_cost += BinaryTree.cost_of_products(code, quantity)
    print(f'Total price: {total_cost}')
except ValueError:
    print("U have incorrect input")
