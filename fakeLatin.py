def main():
    
    #program for pig latin
    END = 'ay'
    word = input("Enter a word: ")
    firstLetter = word[0]


    print("The word", word, "in fake Latin is", word[1: ] + firstLetter + END)
    

if __name__ == '__main__':
    main()
