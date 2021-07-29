from pool_table import PoolTable 

pool_tables = [] 

for index in range(1, 13): 
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

print("1. Checkout table")
print("2. Check-in Table")
print("3. View Tables")

while True: 
    choice = input("Enter choice: ")
    if choice == "1": 
        table_number = input("Which table number: ")
        pool_table = pool_tables[table_number - 1]
        pool_table.check_out() 

import datetime 

class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number 
        self.is_occupied = False 
        self.start_time = None 
        self.end_time = None 
    
    def check_out(self): 
        self.is_occupied = True
        self.start_time = datetime.datetime.now()
    
    def check_in(self): 
        self.is_occupied = False 
        self.end_time = datetime.datetime.now() 
    
    def time_played(self): 
        return self.end_time - self.start_time 

   {"table_number": 10, "is_occupied": false}     

   