class Contact:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open('contact.txt', 'r') as file:
                content = file.read()
                lines = content.splitlines()
                self.contact_count = 0
                for line in lines:
                    if line.startswith("Contact"):
                        self.contact_count += 1
        except FileNotFoundError:
            self.contact_count = 0

    def add_contact(self):
        name = input("Enter name: ")
        number = input("Enter number: ")

        if len(number) != 10 or not number.isdigit():
            print("Invalid number. Please enter a 10-digit phone number.")
            return
        
        if not (number.startswith("98") or number.startswith("97")):
            print("Phone number must start with 98 or 97.")
            return
        
        email = input("Enter email: ")
        contact = {"name": name, "number": number, "email": email}
        self.contacts.append(contact)
        self.contact_count += 1

        with open('contact.txt', 'a+') as file:
            file.write(f"\nContact {self.contact_count}\n")
            file.write(f"Name: {name}\nNumber: {number}\nEmail: {email}\n\n")

        print("Contact added successfully.")
        print("-" * 20)

    def view_contact(self):
        if not self.contacts:
            print("No contacts found.")
            print("-" * 20)
        else:
            print("\nContact list:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}")
                print(f"Number: {contact['number']}")
                print(f"Email: {contact['email']}")
                print("-" * 20)

def main():
    contact_manager = Contact()

    try:
        with open('contact.txt', 'r') as file:
            content = file.read()
            if "Welcome to Contact" not in content:
                with open('contact.txt', 'a+') as file:
                    file.write("Welcome to Contact\n")
                    file.write("-" * 20 + "\n")
    except FileNotFoundError:
        with open('contact.txt', 'w') as file:
            file.write("Welcome to Contact\n")
            file.write("-" * 20 + "\n")

    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contact()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid input, please choose again.")

if __name__ == "__main__":
    main()
