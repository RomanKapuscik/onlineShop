from products import products
from cluster_connection import cluster

db = cluster['onlineShopDB']
collection = db['products']


def initialize_products_collection():
    collection.drop()
    collection.insert_many(products)


def get_price(item: str):
    products = collection.find({})
    for product in products:
        if product['name'] == item:
            return product['price']
