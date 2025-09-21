# contact_book.py

def add_contact(contacts):
    """Adds a new contact to the list."""
    print("\nEnter new contact details:")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"\nContact for '{name}' added successfully!")

def view_contact_list(contacts):
    """Displays a summary list of all contacts."""
    print("\n----- Contact List -----")
    if not contacts:
        print("Your contact book is empty.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
    print("------------------------\n")

def search_contact(contacts):
    """Searches for a contact by name or phone number and displays details."""
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            found_contacts.append(contact)

    print("\n----- Search Results -----")
    if not found_contacts:
        print("No contacts found matching your search.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)
    print("--------------------------\n")


def update_contact(contacts):
    """Updates an existing contact's details."""
    view_contact_list(contacts)
    if not contacts:
        return

    try:
        contact_num = int(input("Enter the contact number to update: "))
        if 1 <= contact_num <= len(contacts):
            contact = contacts[contact_num - 1]
            print("\nEnter new details (leave blank to keep current value):")
            
            new_name = input(f"Name ({contact['name']}): ")
            new_phone = input(f"Phone ({contact['phone']}): ")
            new_email = input(f"Email ({contact['email']}): ")
            new_address = input(f"Address ({contact['address']}): ")

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            
            print("\nContact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    """Deletes a contact from the list."""
    view_contact_list(contacts)
    if not contacts:
        return

    try:
        contact_num = int(input("Enter the contact number to delete: "))
        if 1 <= contact_num <= len(contacts):
            removed_contact = contacts.pop(contact_num - 1)
            print(f"\nContact '{removed_contact['name']}' has been deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def contact_book_app():
    """Main function to run the Contact Book application."""
    contacts = []

    while True:
        print("\nWelcome to the Contact Book!")
        print("1. Add a new contact")
        print("2. View contact list")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    contact_book_app()
