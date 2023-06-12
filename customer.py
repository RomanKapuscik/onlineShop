from cluster_connection import cluster
from shopping_cart import ShoppingCart
import datetime


class Customer:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.cluster = cluster
        self.db = self.cluster['onlineShopDB']
        self.collection = self.db['customers']

    def __check_if_name_in_db(self, name: str, surname: str) -> bool:
        results = self.collection.find({'name': name, 'surname': surname})
        for result in results:
            if result['name'] == name:
                if result['surname'] == surname:
                    return True
        return False

    def add_new_customer(self):
        if not self.__check_if_name_in_db(self.name, self.surname):
            self.collection.insert_one({'name': self.name, 'surname': self.surname, 'orders': []})
            return True
        else:
            return False

    def add_cart_to_customer(self, shopping_cart: ShoppingCart):
        self.add_new_customer()
        self.collection.update_one({'name': self.name, 'surname': self.surname},
                                   {'$push': {'orders':
                                       {
                                           'products': shopping_cart.items,
                                           'total': shopping_cart.get_total_price(),
                                           'order_data_time': datetime.datetime.utcnow(),
                                           'status': 'new'
                                       }}})
# client_1 = Customer('Adam', 'Nowak')
# client_1.add_new_customer()
