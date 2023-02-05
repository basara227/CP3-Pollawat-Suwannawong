print("Enter your Username and Password")
user = input("Username :")
password = (input("Password :"))
if user == "admin" and password == "1234" :
    print("---------------------------")
    print("---Welcome To Amway shop---")
    print("---------------------------")
    print("")
    print("please select an option below")
    Allplant = 1100
    Berry = 1347
    Chocolate = 1313
    print("---------------------------")
    print("Choose 1 = All plant x 1  :", Allplant, "THB")
    print("Choose 2 = Berry  x 1  :", Berry, "THB")
    print("Choose 3 = Chocolate x 1  :", Chocolate, "THB")
    Choose = int(input("Choose :"))

    if Choose == 1:
        item = "All plant"
        number = int(input("Enter number of item :"))
        total = Allplant * number

    elif Choose == 2:
        item = "Berry"
        number = int(input("Enter number of item :"))
        total = Berry * number
    elif Choose == 3:
        item = "Chocolate"
        number = int(input("Enter number of item :"))
        total = Chocolate * number

        print("---------------------------")

        print(item, ">>>>>>>>>>>>>>", "x", number)
        print("total =", total, "THB")
        print("VAT = 7%", total * 7 / 100, "THB")
        total += total * 7 / 100
        print("total VAT included =", total, "THB")

    else:
        item = "Please choose the number between 1-3"
        number = 0
        total = 0
    print("---------------------------")


elif user == "admin" and password != 1234:
    print("Your password is incorrect, Please try again")
else:
    print("Your username is incorrect, Please try again")

