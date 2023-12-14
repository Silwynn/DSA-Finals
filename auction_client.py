import tkinter as tk
from tkinter import messagebox


class Product:
    def __init__(self, product_name, product_description, product_starting_price, owner):
        self.product_name = product_name
        self.product_description = product_description
        self.product_starting_price = product_starting_price
        self.owner = owner


class User:
    def __init__(self, user_name):
        self.user_name = user_name


class AuctionHouse:
    def __init__(self):
        self.users = []
        self.products = []

    def add_user(self, user_name):
        self.users.append(User(user_name))

    def add_product(self, product_name, product_description, product_starting_price, owner):
        self.products.append(Product(product_name, product_description, product_starting_price, owner))

    def display_products(self):
        message = "Products: \n\n"
        for product in self.products:
            message += f"Name: {product.product_name}\nDescription: {product.product_description}\nStarting Price: {product.product_starting_price}\nOwner: {product.owner}\n\n"
        messagebox.showinfo("Products", message)



def create_user():
    user_input = input("Enter your name or 'quit' to exit: ")
    if user_input.lower() == "quit":
        return None
    return user_input


def create_product():
    product_name = input("Enter the product name: ")
    product_description = input("Enter the product description: ")
    product_starting_price = float(input("Enter the starting price: "))
    owner = input("Enter the owner's name: ")
    return product_name, product_description, product_starting_price, owner


def main():
    auction_house = AuctionHouse()

    # GUI Code
    def create_user_gui():
        user_name = user_name_entry.get()
        if user_name:
            auction_house.add_user(user_name)
            user_name_entry.delete(0, tk.END)

    def create_product_gui():
        product_name = product_name_entry.get()
        product_description = product_description_entry.get()
        product_starting_price = float(product_starting_price_entry.get())
        owner = owner_entry.get()
        if product_name and product_description and product_starting_price and owner:
            auction_house.add_product(product_name, product_description, product_starting_price, owner)
            product_name_entry.delete(0, tk.END)
            product_description_entry.delete(0, tk.END)
            product_starting_price_entry.delete(0, tk.END)
            owner_entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Auction House")

    user_name_label = tk.Label(root, text="User Name:")
    user_name_label.pack()
    user_name_entry = tk.Entry(root)
    user_name_entry.pack()
    create_user_button = tk.Button(root, text="Create User", command=create_user_gui)
    create_user_button.pack()

    product_name_label = tk.Label(root, text="Product Name:")
    product_name_label.pack()
    product_name_entry = tk.Entry(root)
    product_name_entry.pack()

    product_description_label = tk.Label(root, text="Product Description:")
    product_description_label.pack()
    product_description_entry = tk.Entry(root)
    product_description_entry.pack()

    product_starting_price_label = tk.Label(root, text="Starting Price:")
    product_starting_price_label.pack()
    product_starting_price_entry = tk.Entry(root)
    product_starting_price_entry.pack()

    owner_label = tk.Label(root, text="Owner:")
    owner_label.pack()
    owner_entry = tk.Entry(root)
    owner_entry.pack()

    create_product_button = tk.Button(root, text="Create Product", command=create_product_gui)
    create_product_button.pack()

    display_products_button = tk.Button(root, text="Display Products", command=auction_house.display_products)
    display_products_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()