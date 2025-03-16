class FileHandling_With_List:

    def load_data(self, FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []

    def save_data(self, FILENAME,data):
        with open(FILENAME, "w") as file:
            for item in data:
                file.write(item + "\n")


    def add_item(self):
        item = input("Enter item to add: ")
        data = self.load_data(FILENAME)
        data.append(item)
        self.save_data(FILENAME, data)
        print("Item added successfully.")


    def delete_item(self):
        data = self.load_data(FILENAME)
        print("Current List:", data)
        item = input("Enter item to delete: ")
        if item in data:
            data.remove(item)
            self.save_data(FILENAME, data)
            print("Item deleted successfully.")
        else:
            print("Item not found.")


    def update_item(self):
        data = self.load_data(FILENAME)
        print("Current List:", data)
        old_item = input("Enter item to update: ")
        if old_item in data:
            new_item = input("Enter new value: ")
            index = data.index(old_item)
            data[index] = new_item
            self.save_data(FILENAME, data)
            print("Item updated successfully.")
        else:
            print("Item not found.")


    def display_list(self):
        data = self.load_data(FILENAME)
        print("Current List:", data)

fh = FileHandling_With_List()

FILENAME = "data.txt"

while True:
    print("\nOptions:")
    print("1. Add Item")
    print("2. Delete Item")
    print("3. Update Item")
    print("4. Display List")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        fh.add_item()
    elif choice == "2":
        fh.delete_item()
    elif choice == "3":
        fh.update_item()
    elif choice == "4":
        fh.display_list()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
