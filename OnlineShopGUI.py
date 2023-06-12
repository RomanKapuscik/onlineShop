import tkinter as tk
from products_collection import initialize_products_collection
from cluster_connection import cluster
from shopping_cart import ShoppingCart
from customer import Customer


class OnlineShoppGUI:

    def __init__(self):
        initialize_products_collection()  # Just to fill the shelves with products.
        self.products = [x for x in cluster['onlineShopDB']['products'].find({})]
        self.cart = ShoppingCart()
        self.total_price = 0.0

        self.root = tk.Tk()
        self.root.title('OnlineShop')

        self.client_data_label = tk.Label(self.root, text='Pleas type Your name and surname: ')

        self.client_data_frame = tk.Frame(self.root)
        self.client_data_frame.columnconfigure(0, weight=1)
        self.client_data_frame.columnconfigure(0, weight=2)

        self.name_label = tk.Label(self.client_data_frame, text='Name: ')
        self.name_label.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self.client_data_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.surname_label = tk.Label(self.client_data_frame, text='Surname: ')
        self.surname_label.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.surname_var = tk.StringVar()
        self.surname_entry = tk.Entry(self.client_data_frame, textvariable=self.surname_var)
        self.surname_entry.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.products_frame = tk.Frame(self.root)
        self.products_frame.columnconfigure(0, weight=1)
        self.products_frame.columnconfigure(0, weight=2)
        self.products_frame.columnconfigure(0, weight=3)
        self.products_frame.columnconfigure(0, weight=4)
        self.products_frame.columnconfigure(0, weight=5)

        self.product_check = [tk.IntVar() for x in range(len(self.products))]
        self.product1_label = tk.Label(self.products_frame, text=self.products[0]['name'])
        self.product1_label.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.product1_checkbox = tk.Checkbutton(self.products_frame, variable=self.product_check[0])
        self.product1_checkbox.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.product2_label = tk.Label(self.products_frame, text=self.products[1]['name'])
        self.product2_label.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.product2_check = tk.IntVar()
        self.product2_checkbox = tk.Checkbutton(self.products_frame, variable=self.product_check[1])
        self.product2_checkbox.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.product3_label = tk.Label(self.products_frame, text=self.products[2]['name'])
        self.product3_label.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.product3_checkbox = tk.Checkbutton(self.products_frame, variable=self.product_check[2])
        self.product3_checkbox.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.product4_label = tk.Label(self.products_frame, text=self.products[3]['name'])
        self.product4_label.grid(row=3, column=0, sticky=tk.W + tk.E)
        self.product4_checkbox = tk.Checkbutton(self.products_frame, variable=self.product_check[3])
        self.product4_checkbox.grid(row=3, column=1, sticky=tk.W + tk.E)

        self.product5_label = tk.Label(self.products_frame, text=self.products[4]['name'])
        self.product5_label.grid(row=4, column=0, sticky=tk.W + tk.E)
        self.product5_checkbox = tk.Checkbutton(self.products_frame, variable=self.product_check[4])
        self.product5_checkbox.grid(row=4, column=1, sticky=tk.W + tk.E)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(0, weight=2)
        self.button_add = tk.Button(self.buttons_frame, text='Add', command=self.button_prest)
        self.button_add.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.client_data_label.pack(padx=20, pady=20)
        self.client_data_frame.pack(padx=10, pady=10)
        self.products_frame.pack(padx=10, pady=10)
        self.buttons_frame.pack(padx=10, pady=10)

        self.root.mainloop()

    def button_prest(self):
        if self.name_var.get() or self.surname_var.get():
            idx = 0
            for checkbox in self.product_check:
                if checkbox.get():
                    self.cart.add(self.products[idx]['name'])
                idx += 1
            self.total_price = self.cart.get_total_price()
            print(self.name_var.get(), self.surname_var.get())
            Customer(self.name_var.get(), self.surname_var.get()).add_cart_to_customer(self.cart)
            self.root.destroy()


OnlineShoppGUI()
