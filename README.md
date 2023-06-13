# onlineShop
basic online shop functionality test
prepared for university project with mongodb

MongoDB setup:
cluster name: Cluster0
username: romankapuscik
password: NmmIGDvUgSt12VId
connection string: mongodb+srv://romankapuscik:<password>@cluster0.x23nxsr.mongodb.net/?retryWrites=true&w=majority

The GUI application OnlineShopGUI.py:
1. The application at start is initializing DB with products.
2. Add unique name and surname in entry fields. If the name and surname already exist an order will be added to existing
customer.
3. Check boxes by the products that You want to add to Your order.
4. Click Add button. Application will create customer and add new cart to a customer 
or if customer already exist a new cart will be added to existing customer.
5. All changes can be observed at: https://cloud.mongodb.com/v2/647c6dba4ea5e65cd565c24e#/metrics/replicaSet/647c6e4ede424565fc4377d7/explorer/onlineShopDB/customers/find