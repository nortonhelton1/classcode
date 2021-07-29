import datetime

class PoolTable: 
    def __init__(self, table_number): 
        self.table_number = table_number
        self.start_time = None # null which means the value does not exist 
        self.end_time = None 
        self.is_occupied = False 

    def check_out(self): 
        # check if the table was already occupied 
        # if occupied then DO NOT check out the table 
        self.start_time = datetime.datetime.now()
        self.is_occupied = True 

    def check_in(self): 
        self.end_time = datetime.datetime.now() 
        self.is_occupied = False 
    
    def total_time_played(self): 
        return self.end_time - self.start_time # Make sure to get the correct difference 