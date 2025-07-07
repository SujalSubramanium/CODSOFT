contacts = []

def add():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})

def view():
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search():
    query = input("Enter name or phone: ")
    for c in contacts:
        if query.lower() in c['name'].lower() or query in c['phone']:
            print(c)
            return
    print("Not found.")

def update():
    name = input("Enter name to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            c['address'] = input("New address: ")
            return
    print("Contact not found.")

def delete():
    name = input("Enter name to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            return
    print("Contact not found.")

def main():
    while True:
        print("\n1. Add\n2. View\n3. Search\n4. Update\n5. Delete\n6. Exit")
        ch = input("Choose: ")
        if ch == "1":
            add()
        elif ch == "2":
            view()
        elif ch == "3":
            search()
        elif ch == "4":
            update()
        elif ch == "5":
            delete()
        elif ch == "6":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()