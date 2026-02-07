"""
Project: Smart Coffee Shop Order System
Author: Smavia Amir
Description:
This program allows a customer to order coffee items,
calculates the total bill, and displays the final order summary.
"""

# Coffee menu stored in a dictionary
menu = {
    "espresso": 250,
    "latte": 300,
    "cappuccino": 320,
    "americano": 280
}

def show_menu():
    print("\n--- Coffee Menu ---")
    for item, price in menu.items():
        print(f"{item.title()} : Rs {price}")

def take_order():
    order = {}
    while True:
        choice = input("\nEnter coffee name (or 'done' to finish): ").lower()

        if choice == "done":
            break

        if choice in menu:
            qty = int(input("Enter quantity: "))
            order[choice] = order.get(choice, 0) + qty
            print("Added to order ")
        else:
            print("Sorry, this item is not available ")

    return order

def calculate_bill(order):
    total = 0
    print("\n--- Order Summary ---")
    for item, qty in order.items():
        price = menu[item] * qty
        total += price
        print(f"{item.title()} x {qty} = Rs {price}")
    return total

# Main program
print(" Welcome to Smart Coffee Shop ")

show_menu()
customer_order = take_order()

if customer_order:
    total_bill = calculate_bill(customer_order)
    print(f"\nTotal Bill: Rs {total_bill}")
    print("Thank you for visiting! ")
else:
    print("\nNo order placed. Have a nice day!")
