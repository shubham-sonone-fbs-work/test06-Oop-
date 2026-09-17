
class VEHICLE:
    
    def __init__(self,wheel,person):
        self.wheel = wheel 
        self.person = person
        
    def cal_toll(self):
        print("CALCULATED TOLL: ")
        
class TWO_WHELLER(VEHICLE):
    
    def cal_toll(self):
        toll = 20 
        
        if self.person > 2:
            toll = toll + (self.person - 2) * 10
            
        print("TWO-WHEELER TOLL : ",toll)
        
        
class THREE_WHELLER(VEHICLE):
    
    def cal_toll(self):
        toll = 30 
        
        if self.person > 3:
            toll = toll + (self.person - 3) * 20
            
        print("THREE-WHEELER TOLL : ",toll)
        
        
class FOUR_WHELLER(VEHICLE):
    
    def cal_toll(self):
        toll = 40
        
        if self.person > 4 :
            toll = toll + (self.person - 4) * 40
            
        print("FOUR-WHEELER TOLL : ",toll)
    

class HEAVY_VEHICLE(VEHICLE):
    
    def cal_toll(self):
        toll = 60
        
        if self.person > 6:
            toll = toll + (self.person - 6) * 100
        
        print("HEAVY VEHICLE TOLL : ",toll)
        
# TWO WHEELER
        
t1 = TWO_WHELLER(2,3)
t1.cal_toll()

# THREE WHEELER
th1 =THREE_WHELLER(3,4)
th1.cal_toll()

# FOUR WHEELER
f1 = FOUR_WHELLER(4,5)
f1.cal_toll()

h1 = HEAVY_VEHICLE(6,6)
h1.cal_toll()