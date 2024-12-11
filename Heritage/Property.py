from abc import ABC,abstractmethod


class Property(ABC):#parent class
    def __init__(self,name="",uf="",value="",address = "",area = ""):
        self._name = name
        self._uf = uf
        self._value = value
        self._address = address
        self._area = area
    @property
    def name(self):
        return self._name
    @property
    def uf(self):
        return self._uf
    @property
    def value(self):
        return self._value
    @property
    def address(self):
        return self._address
    @property
    def area(self):
        return self._area
    
    @name.setter
    def name(self,name):
        self._name = name
    @uf.setter
    def uf(self,uf):
        self._uf = uf
    @value.setter
    def value(self,value):
        self._value = value
    @address.setter
    def address(self,address):
        self._address = address
    @area.setter
    def area(self,area):
        self._area = area
        
    '''
     def GetName(self):
        return self._name
    
     def SetName(self,name):
        self._name = name
    '''  
    def detail(self):
        print(self.__dict__)
        
    def calculateTax(self):
        return print(self._value * 0.02)
    
    @abstractmethod
    def suggestedRent(self):
        ...


class ResidentialProperty(Property):#daughter class
    def __init__(self,name="",uf="",value="",address = "",area = ""):
        super().__init__(name,uf,value,address = "",area = "")#pull all the father's things
        self._rooms = 0
        self._pool = 0
        
    def suggestedRent(self):
        return self.value * 0.01
    
class CommercialProperty(Property):#daughter class
    
    def suggestedRent(self):
        return self._value * 0.015
    
    def calculateTax(self):
        match self._uf:
            case "DF":tax = 0.03
            case "RJ":tax = 0.025
            case "SP":tax = 0.04
            case other: tax = 0.02
        
        return print(self._value * tax)
            
    
class RuralProperty:#parent class
    def __init__(self,hectares = "",corral = "",productive = True):
        self._hectares = hectares
        self._corral = corral
        self._productive = productive
        
    def plantingMonth(self,month):
        match int(month):
            case 1:print("Corn")
            case 2:print("Bean")
            case 3:print("Soy")
            case other:print("Cotton")
            
   
            
class Farm(Property,RuralProperty):#daughter class
    
    def suggestedRent(self):
        return self._value * 0.025
    
'''
can no longer instantiate because it has become an "abstract class"

property = Property("Apartment","DF",10000,"Brasilia",area = "2m4")
property.detail()

'''    


house = ResidentialProperty()
house.name = "MY HOUSE"
house.uf = "RJ"
house.value = 200000
house.address = "Rio de Janeiro"
house.area = "230m3"
house.detail()

clinic = CommercialProperty("Clinic","RJ",400000,"Tocantins",area = "100m2")
clinic.detail()
clinic.calculateTax()

farm = Farm("Farm","PI",400000,"Piaui",area = "900m2")
farm.detail()
farm.calculateTax()
farm.plantingMonth(1)