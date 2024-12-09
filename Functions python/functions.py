def sum_total(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiplication(n1,n2):
    return n1 * n2
    
def division(n1,n2):
    if n2 == 0:
        return ("Cannot divide a number by 0")
    else:
        result = n1 / n2
        return result

def calculate(n1,n2,operator):
    
    match operator:
        case '+':return sum_total(n1,n2)
        case '-':return subtract(n1,n2)
        case '*':return multiplication(n1,n2)
        case '/':return division(n1,n2)
        case other: return 'Operator is not valid'

print(calculate(5,10,'+'))
print(calculate(5,10,'-'))
print(calculate(5,10,'*'))
print(calculate(5,0,'/'))
print(calculate(5,10,'o'))


'''
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
result_final = division(n1,n2)
print(f"The result of the division is: {result_final}")
'''