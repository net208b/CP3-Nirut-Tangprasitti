usernameInput = input("username : ")
passwordInput = input("password : ")
price1 = 30
price2 = 40
price3 = 45
price4 = 45
order = "yes"
sum = 0

if usernameInput == "user01" and passwordInput == "212224236":
    print("Welcome to sweet bakery !")
    print("This is our menu")
    print("1. strawberry cupcake : 30 THB")
    print("2. chocolate cake : 40 THB")
    print("3. blueberry cheesepie : 45 THB")
    print("4. cookie : 75 THB")
    while order == "yes":
        print("Please enter the food number to continue.")
        foodNum = int(input(">> "))
        print("Please enter the quantity to continue.")
        foodQuan = int(input(">> "))
        if foodNum == 1:
            price = foodQuan * price1
            sum += price
            food = "strawberry cupcake"
        elif foodNum == 2:
            price = foodQuan * price2
            sum += price
            food = "chocolate cake"
        elif foodNum == 3:
            price = foodQuan * price3
            sum += price
            food = "blueberry cheesepie"
        elif foodNum == 4:
            price = foodQuan * price4
            sum += price
            food = "cookie"
        else:
            print("Error. Please log in ang try again.")
        print("Your order is",food,"x",foodQuan,"=",price,"THB")
        print("Total price is",sum,"THB")
        print("Do you want anything else? (yes/no)")
        order = input(">> ")
    print("Total price is",sum,"THB")
    print("Thank you !")
else:
    print("Your username or password is incorrect.")