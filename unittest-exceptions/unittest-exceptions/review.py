
# Store Model 

stores = [] 

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []
    
    def add_item(self, item): 
        # check if the item is already in store 
        # then add item to the items array 
        # else ignore it 
        pass 

    #def __repr__(self):
    #    return f"{self.name} - {self.address}"

class Item: 
    def __init__(self, name, price): 
        self.name = name 
        self.price = price 



print("1. Add Store: ")
print("2. Add Item to Store: ")
print("3. View All")
print("q. Quit")

while True: 
    choice = input("Enter choice: ")
    if choice == "1": 
        store_name = input("Enter store name: ")
        store_address = input("Enter store address: ")
        store = Store(store_name, store_address)
        stores.append(store)
    elif choice == "2": 
        for index in range(0, len(stores)): 
            store = stores[index]
            print(f"{index + 1} {store.name} - {store.address}")
        
        # 1. HEB 
        # 2. Walmart 
        # 3. Fiesta 

        store_index = int(input("Choose store to add items: "))
        store = stores[store_index - 1]
        item_name = input("Enter item name: ")
        item_price = float(input("Enter price: ")) 
        item = Item(item_name, item_price) 
        # add item to the store 
        #store.add_item(item) # better approach because you can check and run rules 
        store.items.append(item)

    
    elif choice == "3": 
        for store in stores: 
            print(f"{store.name} - {store.address}")
            for item in store.items: 
                print(f"{item.name} - ${item.price}")
        
    
    elif choice == "q": 
        break 



#Stores 
#  - 0 Store 
#       - name 
#       - address
#       - items 
#           0 - Item 
#                 - name 
#                 - price 