airports = {
    "EFHK": "Helsinki-Vantaa Airport",
}

def airport_info():
    while True:
        print("A: Do you want to enter a new airport? OR")
        print("B: Do you want to fetch the information of an existing airport?")
        print("Press ENTER to quit!")
        user_input = str(input("Which type of service would you prefer? (A or B): "))
        if user_input == "A":
            airport_name_info = str(input("Please enter the name of the airport: "))
            airport_code_info = str(input("Please enter the ICAO code of the airport: "))

            if airport_code_info in airports:
                if airport_code_info in airports and airports[airport_code_info] == airport_name_info:
                   print(f"{airport_name_info} exists in our database already!")
                else:
                   print(f"{airport_code_info} exists but with a different name!")
            else:
                airports[airport_code_info] = airport_name_info
                print(f"{airport_name_info} added to the database!")

        elif user_input == "B":
            user_input_code = str(input(" Alright! Please enter the ICAO code of the airport: "))
            if user_input_code in airports:
                print(f"The Airport you were looking for is: {airports[user_input_code]}!")
            else:
                print(f"{user_input_code} does not exist in the database!")

        else:
            print(f"Airports that exist in our database are: {airports}")
            break

airport_info()