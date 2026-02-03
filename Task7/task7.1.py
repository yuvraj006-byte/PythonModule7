seasons = ("winter", "spring", "summer", "autumn")

months = int(input("Enter the number a month (1,12): "))

if 1 <= months <= 12:
    season = seasons[(months % 12) // 3]
    print(f"It is {season} Season")
    if months in (1, 2, 12):
        print("Merry Christmas and a Happy new Year! :)")
    elif months in (3, 4, 5):
        print("Finally! Its Spring! Green Everywhere! :)")
    elif months in (6, 7, 8):
        print("The Snow is gone already! :)")
    else:
        print("The leaves are already falling! :(")
else:
    print("Please enter a valid month")