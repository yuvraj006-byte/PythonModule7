name_set = set()
print_set = set(items.upper() for items in name_set)

while True:
    user_input = input("Please enter a Name: ").lower()

    if user_input == "":
        print("These where the names you Typed!:", print_set)
        break

    if user_input in name_set:
        print("Existing Name")
    else:
        name_set.add(user_input)
        print("New Name")
