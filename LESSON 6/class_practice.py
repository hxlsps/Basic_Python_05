import datetime
#Create a new class with some properties and methods
class Vehicle:
    def __init__(self,name,max_speed=100,color='red',year=1999):
        self.name=name
        self._max_speed=max_speed #protected property
        self.__color=color #private property
        self.year=year #public property

    def get_name(self):
        return self.name

    def get_max_speed(self):
        return self._max_speed

    def get_color(self):
        return self.__color
    
    def get_year_old(self):
        now=datetime.datetime.now().year
        return now-self.year
    
    def __calculate_year_old(self): #private method
        now=datetime.datetime.now().year
        return now-self.year
    
    def get_calculate_year_old(self): #call __calculate by this method
        return self.__calculate_year_old()
    
    def set_color(self,color):
        self.__color=color

    def set_max_speed(self,max_speed):
        self._max_speed=max_speed

#veh_x=Vehicle('Toyota Fortune')
#veh_y=Vehicle('Huyndai Santafre',200,'black',2016)

#print(f'Vehicle information of X - Name: {veh_x.get_name()}, Color: {veh_x.get_color()}')
#print(veh_x.get_calculate_year_old())
#print(f'Vehicle information of Y - Name: {veh_y.get_name()}, Max speed: {veh_y.get_max_speed()}, Year old: {veh_y.get_year_old()}')

class Customer:
    def __init__(self,name,born_year,job):
        self.name=name
        self.born_year=born_year
        self.job=job
    
    def get_name(self):
        return self.name
    
    def get_year_old(self):
        now=datetime.datetime.now().year
        return now - self.born_year

    def get_job(self):
        return self.job
    
    def set_name(self,name):
        self.name=name

    def set_born_year(self,born_year):
        self.born_year=born_year
    
    def set_job(self,job):
        self.job=job

#customer_1=Customer('Loc',2000,None)
#print(customer_1.get_year_old())

#Create a child class 
class Motor(Vehicle):
    def __init__(self,name,max_speed,color,year,engine):
        self.engine=engine
        #Vehicle.__init__(self,name,max_speed,color,year)
        super().__init__(name,max_speed,color,year)

    def get_color(self): #overwrite dad
        return 'Black white'

    # Cannot access private properties from parent classes
    #def get_color(self): 
     #   return self.__color

#create new object for Motor class
motor_x=Motor('Air Blade',100,'black',2007,150)
print(f'Motor information of X - Name: {motor_x.engine}, Color: {motor_x.get_color()}, Max speed: \
{motor_x._max_speed}')
#print(f'Motor information of X - Name: {motor_x.engine}, Color: {motor_x.get_color()}, Max speed: \
#{motor_x._max_speed}, Color: {motor_x.get_color()}')
#Con cung k the truy cap private cua thang cha ma chi co cha moi truy cap duoc thoi