menuList = []
priceList = []

def showbill():
    total = 0
    print("===== MY FOOD =====")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total += int(priceList[number])
    print("Total",total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showbill()
