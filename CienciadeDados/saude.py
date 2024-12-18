import numpy as np
import pandas as pd

class Paciente:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        

pacient = {
    "Paciente 1": Paciente('Maria',25,'F',60,1.70),
    "Paciente 2": Paciente('Ana',30,'F',76,1.64),
    "Paciente 3": Paciente('Pedro',32,'M',90,1.90),
    "Paciente 4": Paciente('Orion',45,'M',80,1.75),
} 

lista_de_pacientes = [p.__dict__ for p in pacient.values()]
df_pacientes = pd.DataFrame.from_records(lista_de_pacientes,index=pacient.keys())


df_pacientes['IMC'] = df_pacientes.apply(lambda i: i.peso / i.altura **2,axis=1)

media = np.mean(df_pacientes['IMC'])

sobrepeso = df_pacientes[df_pacientes['IMC'] > 25]

percentual = len(sobrepeso) / len(df_pacientes)*100

print(f"O percentual de pessoas sobrepeso foi de: {percentual}%")
print(sobrepeso)
print(df_pacientes)