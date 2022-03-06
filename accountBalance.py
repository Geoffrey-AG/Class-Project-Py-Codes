#Geoffrey Gomlak
#CSC119
#1/27/22
#P1.4 Account Balance  

def main():
    initial = 1000
    rate = 0.05
    time = 0
    print("At year", time, "your account has $", initial)
    print()
    time = time + 1
    initial = initial * ( 1 + rate * time)
    print("At year", time, "your account has $", initial)
    print()
    time = time + 1
    initial = initial * ( 1 + rate * time)
    print("At year", time, "your account has $", initial)
    print()
    time = time + 1
    initial = initial * ( 1 + rate * time)
    print("At year", time, "your account has $", initial)
    
        

main()
    
