from donations_pkg.user import login, register
from donations_pkg.homepage import show_homepage, donate, show_donations
 
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
            database[authorized_user] = password
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif choice == "4":
        print("\n--- All Donations ---")
        show_donations(donations)
    elif choice == "5":
        print("Bye!")
        break
