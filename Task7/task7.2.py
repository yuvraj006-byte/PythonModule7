name_set = set()

while True:
    user_input = input("Please enter a Name (PRESS ENTER TO END): ").lower()

    if user_input != "":
        if user_input not in name_set:
            name_set.add(user_input)
            print("New Name")
        elif user_input in name_set:
            print("Existing Name")

    else:
        output = [n for n in name_set]
        print("GoodBye!")
        print("These where the names you Typed!:", output)
        break


