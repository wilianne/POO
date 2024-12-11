class Product:
    def __init__(self,name="",value="",quantidade = 0,mark="",model=""):
        self.name = name
        self.value = value
        self.quantidade = quantidade
        self.mark = mark
        self.model = model
    def buy(self,quantidade):
        self.quantidade += quantidade  

    def sell(self,quantidade):
        if quantidade > self.quantidade:
            print("*************************************************")
            print("Not enough stock")
            print(f"Maximum quantity: {self.quantidade}")
            print("*************************************************")
        else:
            self.quantidade -= quantidade
    
product0 = Product("Smartphone",1000,100,"LG","L231")
product0.buy(10)
product0.sell(800)

product1 = Product("Fridge",2300,50,"Samsung","12345")


product2 = Product("Notebook",5600,"Dell","G15")
product2.buy(100)
product2.sell(1)



print(product0.__dict__)
print(product1.__dict__)
print(product2.__dict__)