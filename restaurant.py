import os
import random

# Function to clear terminal
def clear_terminal():
    os.system('cls||clear')

# Menu items, prices, and codes
menu = {
    1: {'name': 'French Fries', 'price': 2.00},
    2: {'name': '1/4 Pound Burger', 'price': 5.00},
    3: {'name': '1/4 Pound Cheese Burger', 'price': 5.55},
    4: {'name': '1/2 Pound Burger', 'price': 7.00},
    5: {'name': '1/2 Pound Cheeseburger', 'price': 7.50},
    6: {'name': 'Medium Pizza', 'price': 9.00},
    7: {'name': 'Medium Pizza + Extra Toppings', 'price': 11.00},
    8: {'name': 'Large Pizza', 'price': 12.00},
    9: {'name': 'Large Pizza + Extra Toppings', 'price': 14.50},
    10: {'name': 'Garlic Bread', 'price': 4.50}
}

# Function to print menu
def print_menu():
    print('MENU')    
    print('---------------------------------------------------------')
    print('Code\tItem\t\t\t\t\tPrice')
    print('---------------------------------------------------------')
    for code, item in menu.items():
        print(f'{code}\t{item["name"]:<30}\t\t${item["price"]:.2f}')
    print('---------------------------------------------------------')


# Initialize variables
def get_order():
    order = []
    total_price = 0

    # Ask for order
    while True:
        # Ask for item number
        item_num = int(input('Enter the item number you want to order: '))
        while item_num not in menu:
            item_num = int(input('Invalid item number. Please enter a valid item number: '))

        # Ask for quantity
        quantity = int(input('Enter the quantity you want to order: '))
        while quantity < 1:
            quantity = int(input('Invalid quantity. Please enter a valid quantity: '))

        # Add item to order list
        order.append((item_num, quantity))

        # Ask if they want to order anything else
        more = input('Do you want to order anything else? (y/n): ')
        while more.lower() not in ['y', 'n']:
            more = input('Invalid input. Please enter y or n: ')
        if more.lower() == 'n':
            break

    # Calculate total price
    for item in order:
        item_num = item[0]
        quantity = item[1]
        total_price += menu[item_num]['price'] * quantity

    return order, total_price

# Print receipt
def print_receipt(order, total_price):
    clear_terminal()
    print('Items Ordered\t\t\t\t\tPrice')
    print('---------------------------------------------------------')
    for item in order:
        item_num = item[0]
        quantity = item[1]
        print(f'{quantity} {menu[item_num]["name"]:<30}\t\t${menu[item_num]["price"] * quantity:.2f}')
    print('---------------------------------------------------------')
    print(f'Total\t\t\t\t\t\t${total_price:.2f}')
    print(f'Order Number:\t\t\t\t\t{random.randint(1000, 9999)}')
    print('---------------------------------------------------------')

# Print menu
print_menu()

# Get order
order, total_price = get_order()

# Print receipt
print_receipt(order, total_price)
