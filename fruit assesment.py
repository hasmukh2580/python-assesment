fruit_stock = {}
menu="""
    WELCOME TO FRUIT MARKET
        
    1.Manager
    2.Customer
    """
print(menu)
role = int(input("Select your role : "))


while True:
 if role==1:
    print("\n1. Add Fruit to Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter fruit name: ")
        price = int(input("Enter price per unit: "))
        quantity = int(input("Enter quantity to add: "))
        if name in fruit_stock:
            fruit_stock[name]['quantity'] += quantity
        else:
            fruit_stock[name] = {'price': price, 'quantity': quantity}
        print(f"{quantity} {name}(s) added to the stock.")
        a = input("Do you want to perform more operation :(y/n) : ")
        if a == "y":
                continue
        elif a == "n":
                break
    elif choice == '2':
        print("Current Fruit Stock:")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: Price: {details['price']} Quantity: {details['quantity']}")
        a = input("Do you want to perform more operation :(y/n) : ")
        if a == "y":
                continue
        elif a == "n":
                break
    elif choice == '3':
        name = input("Enter fruit name to update: ")
        if name in fruit_stock:
            new_quantity = int(input("Enter new quantity: "))
            fruit_stock[name]['quantity'] = new_quantity
            print(f"{name} stock updated to {new_quantity}.")
        else:
            print(f"{name} is not in the stock.")
        a = input("Do you want to perform more operation :(y/n) : ")
        if a == "y":
                continue
        elif a == "n":
                break    
    