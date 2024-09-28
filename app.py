from donations_pkg.user import login, register
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
    choice = input("Choose an option: ")
    if choice == "1":
        username = input("\nEnter username: ")
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("\nEnter username: ")
        password = input("Enter Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password
    elif choice == "3":
        print("TODO: Write Donate Functionality")
    elif choice == "4":
        print("TODO: Write Show Donations Functionality")
    elif choice == "5":
        print("Bye!")
        break
