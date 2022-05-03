def main():

    amountPaid = input("Enter the amount you paid: ")
    itemCost = input("Enter the cost of the item: ")
    change = float(amountPaid) - float(itemCost)
    dollars = 100
    qaurters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    print("You paid", amountPaid, "for a item that costs", itemCost)
    print("Your change will be", change)

    changeInCents = change * 100
    dollars = changeInCents // 100

    print("You got", dollars, "dollars")

main()
    
