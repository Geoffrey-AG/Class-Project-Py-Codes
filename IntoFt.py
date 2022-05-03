def main():

    feet = input('Enter a length in inches: ')
    CONVERT = 12
    
    feet1 = int(feet) // CONVERT

    inch = feet % CONVERT
    
    print(f'{feet} in. = {feet1}\' {inch}'' ')
    

    
if __name__ == '__main__':
        main()
