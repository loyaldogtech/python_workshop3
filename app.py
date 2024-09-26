from donations_pkg.homepage import show_homepage

database = {
    "admin": "password123",
}

donations = []

authorized_user = ""

show_homepage()
if authorized_user == "":
    print("You must be logged in to donate")
else:
    print(f"Logged in as {authorized_user}")

while True:
    choice = input("What would you like to do? ").lower()
    if choice == "1":
        print("TODO: Write Login Functionality")
    elif choice == "2":
        print("TODO: Write Register Functionality")
    elif choice == "3":
        print("TODO: Write Donate Functionality")
    elif choice == "4":
        print("TODO: Write Show Donations Functionality")
    elif choice == "5":
        print("Bye!")
        break
