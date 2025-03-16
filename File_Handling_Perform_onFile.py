def read():
    f = open("task.txt", "r")
    print(f.read())
    f.close()

def write():
    f = open("task.txt", "w")
    print(f.write())
    f.close()

def update_specific(olddata, newdata):
    filename = "task.txt"
    file = open(filename, "r")

    f = file.read()
    if olddata in f:

        f = f.replace(olddata, newdata, 1)
        file = open(filename, "w")
        file.write(f)
        print("Update Sucessfully")


def add_specific(olddata, newdata, position):
    filename = "task.txt"
    file = open(filename, "r")

    f = file.read()
    if olddata in f:
        if position == "before":
            f = f.replace(olddata, newdata + olddata, 1)
        else:
            f = f.replace(olddata, olddata + newdata, 1)

        file = open(filename, "w")
        file.write(f)
        print("Add Sucessfully")
    else:
        print("Data Not Found")


def delete_specific(delkaro):
    filename = "task.txt"

    file = open(filename, "r")
    f = file.read()

    if delkaro in f:
        f = f.replace(delkaro, "", 1)
        file = open(filename, "w")
        file.write(f)
        print("Delete Sucessfully")

while True:
    print("\nOptions:")
    print("1. Update Item")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Display List")
    print("5. Exit")
    

    choice = input("Do you want to Add or Update or Delete?").strip().lower()

    if choice == "1":
        olddata = input("Enter old data :")
        newdata = input("Enter new data :")
        update_specific(olddata, newdata)

    elif choice == "2":
        olddata = input("Enter old data :")
        newdata = input("Enter new data You Add :")
        position = input("Add data before/after current :").strip().lower()
        add_specific(olddata, newdata, position)

    elif choice == "3":
        delkaro = input("Enter the word to delete :")
        delete_specific(delkaro )
    
    elif choice == "4":
        read()

    elif choice == "5":
        print("Exit Program.")
        break

    else:
        print("Invalid choice.")
