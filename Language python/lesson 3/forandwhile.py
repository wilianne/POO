goOn = True
while goOn:
    
    n = int(input("Enter a number: "))
    for i in range(11):
        print(f"{n} X {i} = {n* i}")
    
    goOn = input("Want to continue: ")
    goOn = True if goOn == 'yes' else False
    
