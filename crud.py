from utils import create, retrieve, update, delete

def user_flow():
    while True:
        print("\nChoose an action:")
        print("1. Create")
        print("2. Retrieve")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the district to be added: ")
            create({'name': name})
        elif choice == '2':
            district_id = int(input("Enter the id of the district to retrieve: "))
            district = retrieve(district_id)
            if district:
                print("Retrieved district:", district)
            else:
                print("District not found.")
        elif choice == '3':
            district_id = int(input("Enter the id of the district to update: "))
            new_name = input("Enter the new name for the district: ")
            update(district_id, new_name)
        elif choice == '4':
            district_id = int(input("Enter the id of the district to delete: "))
            delete(district_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    user_flow()
