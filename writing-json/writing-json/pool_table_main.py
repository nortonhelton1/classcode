
from pool_table import PoolTable 

pool_tables = [] 

# create 12 pool tables 
for index in range(1,13): 
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

print(pool_tables)

pt = pool_tables[1]
pt.check_out() 

def turn_light_on(status): # makes a copy of the value 
    status = False 

is_on = True 
turn_light_on(is_on)
print(is_on)

