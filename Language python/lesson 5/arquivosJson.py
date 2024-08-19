import json
pessoas =[
    {'nome':'orion','telefone':'(61)9999-8764'},
    {'nome':'maria','telefone':'(61)9456-2214'},
    {'nome':'orion','telefone':'(61)5789-1111'}
]

with open('pessoas.json','w') as arquivo:
    json.dump(pessoas,arquivo)