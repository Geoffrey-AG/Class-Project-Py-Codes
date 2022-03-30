'''
Name: Geoffrey Gomlak
Class: CSC 119
Program: Cilvillian time to Military Time
Date: 3/12/22
Updated: 3/29/22
'''

def main():
    
    hour = int(input("Enter the hour: "))
    print()
    

    if hour >= 1 and hour <= 12:

        suffix = input("Enter the suffix: ")
        suffix = suffix.lower()
    
        if suffix == 'pm':

            print("The military time is", hour + 12, ":00")
            

        if suffix == 'am':
            print("The military time is", hour, ":00")
            

        else:
            print("Error: The suffix must be am or pm")
            main()
    else:
        print("Error: The hour must be between 1 and 12")
        main()
        
if __name__ == '__main__':
    main()
