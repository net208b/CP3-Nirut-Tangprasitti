def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return show_menu()
    else:
        print("Your username or password is incorrect. Please try again.")
        return login()

def show_menu():
    print("Done !")
    print("-------- 1Shop --------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menu_select()

def menu_select():
    userSelected = input(">>")
    if userSelected == "1":
        total_price = float(input("Price (THB) : "))
        print("Total price :",vat_calculator(total_price),"THB")
    elif userSelected == "2":
        print("Total price :",price_calculator(),"THB")

def vat_calculator(total_price):
    vat = 7
    result = total_price + (total_price * vat / 100)
    return result

def price_calculator():
    price1 = int(input("first priduct price (THB) : "))
    price2 = int(input("second priduct price (THB) : "))
    return vat_calculator(price1+price2)

login()
