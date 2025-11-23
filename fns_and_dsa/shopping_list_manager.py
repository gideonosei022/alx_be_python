# shopping_list_manager.py

shopping_list = []  # Start with an empty list

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping_list.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping_list.")
            else:
                print(f"'{item}' not found in the shopping_list.")

        elif choice == '3':
            print("\nCurrent Shopping List:")
            for item in shopping_list:
                print(item)
            if not shopping_list:
                print("Your shopping_list is empty.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
