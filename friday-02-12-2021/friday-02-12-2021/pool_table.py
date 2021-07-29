
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