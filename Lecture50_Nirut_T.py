def addnumber(x,y):
    print("The answer is",x+y)
def subnumber(x,y):
    print("The answer is",x-y)
def mulnumber(x,y):
    print("The answer is",x*y)
def divnumber(x,y):
    print("The answer is",x/y)

print("calculator program")
print("please select function")
print("1. + | 2. - | 3. x | 4. /")
userChoose = input(">> ")
if userChoose != "1" and userChoose != "2" and userChoose != "3" and userChoose != "4":
    print("Error. Please try again.")
else:
    x = int(input("first number : "))
    y = int(input("second number : "))
    if userChoose == "1":
        addnumber(x,y)
    elif userChoose == "2":
        subnumber(x,y)
    elif userChoose == "3":
        mulnumber(x,y)
    elif userChoose =="4":
        divnumber(x,y)
