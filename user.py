def wel(urn):
    money = 0
    print("Welcome", urn)
    print()
    ask4 = input("1) Add Money, 2) Take Money, 3) Stats, 4)Log Out")
    if ask4 == '4':
        main()
    elif ask4 == '2':
        print()
        sub = input("How much do you want to take?: ")
        money = money - int(sub)
        wel(urn)
    elif ask4 == '1':
        print()
        add = input("How much do you want to add?: ")
        money = money + int(add)
        wel(urn)
    elif ask4 == '3':
        print()
        print("---Stats---")
        print()
        print("Total Money: ", money)
        print()
        wel(urn)
      
def pro(urn, pas):
    ask1 = input("Enter your user name: ")
    if ask1 == urn:
        print()
        ask2 = input("Enter your pass word: ")
        if ask2 == pas:
            print()
            wel(urn)
        else:
            print()
            print("Wrong password try again")
            pro(urn, pas)
    else:
        print()
        print("Wrong user name try again")
        pro(urn, pas)



def main():
    print("---Money---")
    print()
    ask3 = input("1) New Login, 2)Sign In 3) Exit")
    if ask3 == '1':
        urn = input("Enter a user name: ")
        pas = input("Enter a pasword: ")
        print()
        pro(urn, pas)
    elif ask3 == '2':
        pro(urn, pas)
    elif ask3 == '3':
        exit
    else:
        print("Error...Try again")
        main()
    

main()
