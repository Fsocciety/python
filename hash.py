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
    hash = (ord(string[0]) - 97) % 26
    return hash

def read():
    search = input("Search product: ")
    product_index = hash_function(search)
    product_index = int(product_index)
    if products[product_index]:
        for item in products[product_index]:
            for key, value in item.items():
                if key == search:
                    print(f"{key}: ${value}")
                else:
                    print(f"{search.title()} doesn't exist!")
    else:
        print(f"{search.title()} doesn't exist!")



while True:
    (product, price) = ask()
    index = hash_function(product)
    add(index, product, price)
    read()
