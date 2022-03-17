def main():

    SHIFT = 3
    encrypted = ''
    decrypted = ''


    ask = input('1) Encrypted, 2) Decrypted, 3)Exit ')
    print()
    if ask == '1':
        message = input('Enter a message: ')
        for i in message:
            e = ord(i) + SHIFT
            encrypted =  encrypted + chr(e)
        print('The Encrypted message is:', encrypted)
        print()
        main()
    elif ask == '2':
        word = input('Enter the encrypted message: ')
        for i in word:
            d = ord(i) - SHIFT
            decrypted =  decrypted + chr(d)
        print('The Encrypted message is:', decrypted)
        print()
        main()
    elif ask == '3':
        exit
    else:
        print('Error')
        main()
            

if __name__=='__main__':
    main()
