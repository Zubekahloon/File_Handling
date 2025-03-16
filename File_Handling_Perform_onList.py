def user_save_list(user_list):
    f = open("taskk.txt", "w")
    for item in user_list:
        f.write(item + "\n")
        

def read():
    f = open("taskk.txt", "r")
    print(f.read())
    f.close()

def write():
    f = open("taskk.txt", "w")
    print(f.write())
    f.close()

def update_specific(olddata, newdata):
    filename = "taskk.txt"
    file = open(filename, "r")

    f = file.read()
    if olddata in f:

        f = f.replace(olddata, newdata, 1)
        file = open(filename, "w")
        file.write(f)
        print("Update Sucessfully")


def add_specific(olddata, newdata, position):
    filename = "taskk.txt"

    
    f = open(filename, "r")
    lines = f.readlines() 

    lines = [line.strip() for line in lines]

    if olddata in lines:
        index = lines.index(olddata) 
        if position == "before":
            lines.insert(index, newdata)
        else:
            lines.insert(index + 1, newdata)

        
        f = open(filename, "w")
        f.write("\n".join(lines) + "\n")  # Convert list back to string

        print("Added Successfully")
    else:
        print("Data Not Found")



def delete_specific(delkaro):
    filename = "taskk.txt"

    file = open(filename, "r")
    f = file.read()

    if delkaro in f:
        f = f.replace(delkaro, "", 1).strip()
        file = open(filename, "w")
        file.write(f)
        print("Delete Sucessfully")

def display_list():
    f = open("taskk.txt", "r")
    print(f.read())


# Get list input from user

user_list = input("Enter a list of items separated by commas: ").split(",")
user_list = [item.strip() for item in user_list]

user_save_list(user_list)
print("List saved successfully.")

# Menu for operations
while True:
    print("\nOptions:")
    print("1. Update Item")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Display List")
    print("5. Exit")

    choice = input("Do you want to Add or Update or Delete? (add/update/delete): ").strip().lower()

    if choice == "1":
        olddata = input("Enter old data :")
        newdata = input("Enter new data :")
        update_specific(olddata, newdata)

    elif choice == "2":
        olddata = input("Enter old data (already exit):")
        newdata = input("Enter new data You Add :")
        position = input("Add data before/after current :").strip().lower()
        add_specific(olddata, newdata, position)

    elif choice == "3":
        delkaro = input("Enter the word to delete :")
        delete_specific(delkaro)
    
    elif choice == "4":
        display_list()
    
    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
