num = int(input("Enter the num: "))

if(num == 0):
    print("num is 0")

elif(num > 0):
    
    if(num <= 10):
        print("number is between (1)-(10)")
    
    elif(num <= 20):
        print("num is between (11)-(20)")
    
    elif(num <= 30):
        print("num is between (21)-(30)")
    
    else:
        print("num is greater than 30")

else:
    print("num is negative")