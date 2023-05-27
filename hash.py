# size = input("Size of array: ")

products = [[]] * 26

def ask():
    product = input("Enter product name: ")
    price = input(f"Enter price for {product}: ")
    return product, price


def add(index, product, price):
    dictionary = {product: price}
    if products[index] == []:
        products[index] = [dictionary]
    else:
        products[index].append(dictionary)
    print(products)

def hash_function(string):
    string.lower()
    hash = (ord(string[0]) + 3) % 26
    return hash

while True:
    (product, price) = ask()
    index = hash_function(product)
    add(index, product, price)
