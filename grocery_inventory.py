# Initialize dictionaries to store grocery items and their quantities,items used, and items left.
groc = {}
groc_used = {}
items_left = {}


# Function to load data from files.
def load_data():
    try:
        # Load data from groc_data.txt file into 'groc' dictionary.
        with open('groc_data.txt', 'r') as groc_file:
            for i in groc_file:
                key, value = i.strip().split(':')
                value = int(value)
                groc[key] = value
        # Load data from items_left.txt file into 'items_left' dictionary.
        with open('items_left.txt', 'r') as items_file:
            for j in items_file:
                key, value = j.strip().split(':')
                value = int(value)
                items_left[key] = value
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting with empty lists.")


# Function to save data to files.
def save_data():
    with open('groc_data.txt', 'w') as groc_file:
        for key, value in groc.items():
            groc_file.write(f"{key}:{value}\n")
    with open('items_left.txt', 'w') as items_file:
        for key, value in items_left.items():
            items_file.write(f"{key}:{value}\n")


# Function to save review data to a file.
def save_review_data():
    try:
        with open('review_data.txt', 'w') as file:
            file.write("------Items left-------\n")
            for item, quantity in items_left.items():
                file.write(f"{item}: {quantity} grams\n")
            file.write("--------------------------\n")
    except Exception as e:
        print("An error occurred while saving review data:", e)


# Function to add or update an item in the grocery list.
def add_or_update_item(item, quantity):
    if item not in groc:
        groc[item] = quantity
        items_left[item] = quantity
        print(f"---Added {quantity} grams of {item} to the list---")
        save_data()
    else:
        print("Item already exists in the list")
        response = input("Do you want to update the required quantity (Y/N): ").upper()
        if response == 'Y':
            groc[item] += quantity
            items_left[item] += quantity
            print("-----Required quantity updated-----")
            save_data()


# Function to mark an item as used and update quantities.
def used_item(item, used_quantity):
    if item in groc:
        if item not in groc_used:
            groc_used[item] = 0
        if items_left[item] >= used_quantity:
            groc_used[item] += used_quantity
            items_left[item] -= used_quantity
            print(f"----Used {used_quantity} grams of {item}----")
            save_data()
        else:
            print(f"   Not enough {item} in stock.   ")
    else:
        print(f"{item} is not in the grocery list.")


# Function to review items left in stock.
def review_items_left():
    try:
        with open('items_left.txt', 'r') as file:
            print("------Items left-------")
            for i in file:
                key, value = i.strip().split(':')
                print(f"{key}: {value} grams")
            print("--------------------------")
    except FileNotFoundError:
        print("No review data found.")


# Function to view all items in the grocery list.
def view_list_items():
    print("List of items:")
    print("-------------------------")
    for item, quantity in groc.items():
        print(f"{item}: {quantity} grams")
    print("-------------------------")


# Function to display the main menu of operations.
def operation():
    print()
    print("1. Add a new item to the list / Update required quantity")
    print("2. Update used quantity")
    print("3. Review items left")
    print("4. View your list")
    print("5. Exit")
    print()


# Function to handle user input and execute operations.
def choice():
    while True:
        operation()
        ch = int(input("Enter your choice: "))
        if ch == 1:
            item = input("Enter the item to be added: ")
            quantity = int(input("Enter the quantity in grams: "))
            add_or_update_item(item, quantity)
            save_review_data()
        elif ch == 2:
            item = input("Enter the item: ")
            quantity = int(input("Enter the used quantity in grams: "))
            used_item(item, quantity)
            save_review_data()
        elif ch == 3:
            review_items_left()
            save_review_data()
        elif ch == 4:
            view_list_items()
        elif ch == 5:
            print("Thank you...Have a great day!")
            save_data()
            save_review_data()
            break
        else:
            print("Invalid selection")


# Load data from files when the program starts.
load_data()
# Start the main program loop.
choice()
