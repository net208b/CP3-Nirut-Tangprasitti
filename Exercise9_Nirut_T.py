usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Your username or password is incorrect. Please try again.")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Welcome!")