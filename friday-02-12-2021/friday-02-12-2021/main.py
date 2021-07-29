
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
