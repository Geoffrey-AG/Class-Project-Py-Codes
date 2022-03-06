def main():
    print()
    print("Celsius <-> Fahrenheit Calculator")
    print()
    print("1)Celsius")
    print("2)Fahrenheit")
    print("3)Exit")
    print()
    #input
    choice = input("---> ")
    if choice == '1':
        print()
        print("Enter a temp. in Celsius")
        #input
        cel = input("---> ")
        print()
        celFah = (float(cel) * 1.8) + 32
        #output
        print("The temp", cel, "°C in fahrenheit is", round(celFah, 2), "°F")
        print()
        main()
    elif choice == '2':
        print()
        print("Enter a temp. in Fahenheit")
        fah = input("---> ")
        #input
        fahCel = (float(fah) - 32) * .5556
        #output
        print("The temp", fah, "°F in celsius if", round(fahCel, 2), "°C")
        print()
        main()
    elif choice == '3':
        exit
    else:
        #easy way to check input
        print()
        print("Error...Try Again")
        main()
if __name__ == "__main__":        
    main()
