# intro 

print("Hey welcome! \n")
print(''' Use these commands to use the calculator :
            Addition = '+'
            substraction = '-'
            multiplication = '*'
            division = '/' ''')
# input 

var1 = input("enter here:")
try:
    var2 = int(input("Enter the number:")) 
    var3 =  int(input("Enter the second number:"))
except:
    print("the input must be a number !!")

try :
    if var1 == '+':
        sum = var2 + var3
        print("your answer is " , sum) 
    elif var1 ==  '-':
        diff = var2 - var3
        print("your answer is " , diff)
    elif var1 == '*':
        times = var2*var3
        print("your answer is " , times)
    elif var1  == '/':
        div = var2/var3
        print("your answer is" , div)
    else:
        print("wrong input ! try again")
except:
        print("Wrong imput !! please try again ")
    
#ez