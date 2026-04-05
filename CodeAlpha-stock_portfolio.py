portfolio = {}

def add_stock():
    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per stock: "))
    
    portfolio[name] = {"quantity": quantity, "price": price}
    print(f"{name} added successfully!")

def view_portfolio():
    total_value = 0
    print("\nYour Portfolio:")
    
    for stock, data in portfolio.items():
        value = data["quantity"] * data["price"]
        total_value += value
        print(f"{stock} -> Quantity: {data['quantity']}, Price: {data['price']}, Value: {value}")
    
    print("Total Investment Value:", total_value)

def main():
    while True:
        print("\n1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

main()