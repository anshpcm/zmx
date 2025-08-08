    item1 = input("item name: ")
    price1 = float(input("Enter price of " + item1 + ": ₹"))
    qty1 = int(input("Enter quantity of " + item1 + ": "))

    item2 = input("item name: ")
    price2 = float(input("Enter price of " + item2 + ": ₹"))
    qty2 = int(input("Enter quantity of " + item2 + ": "))

    total1 = price1 * qty1
    total2 = price2 * qty2
    grand_total = total1 + total2

    print("\n------ Shopping Bill ------")
    print(item1, "x", qty1, "= ₹", total1)
    print(item2, "x", qty2, "= ₹", total2)
    print("----------------------------")
    print("Total = ₹", grand_total)
