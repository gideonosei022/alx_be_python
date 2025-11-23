shopping_list = []  # Start with an empty list

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")  # Menu includes exit option

while True:
    display_menu()  # Continuously display menu
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add an item
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")

    elif choice == '2':
        # Remove an item
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f"'{item}' not found in the shopping list.")

    elif choice == '3':
        # Display the shopping list
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
        if not shopping_list:
            print("Your shopping list is empty.")

    elif choice == '4':
        # Exit the program
        print("Exiting the Shopping List Manager. Goodbye!")
        break

    else:
        # Handle invalid menu choices
        print("Invalid choice. Please enter a number from 1 to 4.")