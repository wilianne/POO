numbers = [4,8,9,3]

result =[]

'''
for n in numbers:
    result.append(n*2)
def multiplication(n):
    return n*2 
result = map(multiplication,numbers)#will transform into a map type object
#need to convert to list to work
print(numbers,list(result))
'''

   
result = map(lambda n:n*2,numbers)#create an anonymous function
print(numbers,list(result))