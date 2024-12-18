import data
class Categoria:
    def __init__(self,tipo =""):
        self.tipo = tipo
        
    def taxaAgua(self,consumo):
        print("Data da leitura: ",data.formatarData())
        match self.tipo:
            case "Clinica": return consumo * 1
            case "Restaurante": return consumo * 2
            case "Hotel": return consumo * 2.5
            case other: return consumo * 1.2


class Imovel:
    
    imposto = 0.2
    
    def __init__(self,nome,quartos,suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()
        
    def __str__(self):
        return str(self.__dict__)
        
    def __add__(self,other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self,other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __lt__(self,other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print("Chamou o metodo estatico sem criar o objeto")
    
    @classmethod
    def metodoClasse(cls):
        print("Chamou o metodo de classe que ve o imposto:",cls.imposto)
        
        
hotel = Imovel("Hotel",4,5)
categoria1 = Categoria("Hotel")
hotel.categoria = categoria1
print(hotel.detalhar())
print(hotel.categoria.taxaAgua(300))

mansao = Imovel("Mansao",6,7)
categoria2 = Categoria("Casa")
mansao.categoria = categoria2

casarao = Imovel("Casarao",2,4)
categoria3 = Categoria("Casa")
casarao.categoria = categoria3




# print(mansao.detalhar())

# hotel.somarAposentos()
# mansao.somarAposentos()

# Imovel.metodoEstatico()
# Imovel.metodoClasse()

# soma = hotel + mansao
# print(soma)
# print(hotel > mansao)
# print(hotel < mansao)