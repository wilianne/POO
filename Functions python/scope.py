n1 = 5
n2 = 8
n3 = 7

def sum_total(n1,n2):

    n1 = 10 #soverwrote the variable n1
    n2 = 20 #overwrote the variable n2

    n4 = 20 #this variable only exists within the function

    print("Sum function: n1",n1)
    print("Sum function: n2",n2)
    print("Sum function: n3",n3)
    print("Sum function: n4",n4)

print("n3 :", n3)#called before the function
sum_total(5,8)

print("n1 :", n1)#value outside the function
print("n2 :", n2)#value outside the function