# Writing Classes to JSON 

import json 

# Python knows how to write the following data types to JSON 
# Int, Float, Boolean, String, Dictionary, Arrays

class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number 
        self.is_occupied = False 
    
    def check_out(self): 
        self.is_occupied = True
    
    def check_in(self): 
        self.is_occupied = False 

    def to_dictionary(self): 
        return self.__dict__ # represents the object as a dictionary __dict__

    @staticmethod
    def pool_table_from_dictionary(dict): 
        p = PoolTable(dict["table_number"])
        p.is_occupied = dict["is_occupied"]
        return p 

        #return {
        #    "table_number": self.table_number, 
        #    "is_occupied": self.is_occupied
        #    } 


pt = PoolTable(10)

#pool_table_dict = pt.to_dictionary()
#print(pool_table_dict)

#print(pt.__dict__)

#with open("pool_tables.json", "w") as file_object: 
#    json.dump(pt.to_dictionary(), file_object)

with open("pool_tables.json") as file_object: 
    pool_table_dict = json.load(file_object)

print(pool_table_dict)

p = PoolTable.pool_table_from_dictionary(pool_table_dict)
