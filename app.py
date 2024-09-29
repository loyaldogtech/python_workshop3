from donations_pkg.user import login, register
from donations_pkg.homepage import show_homepage, donate, show_donations
import re
 
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
        if not re.match("^[a-zA-Z][a-zA-Z0-9]+$", username):
            print("Username must start with a letter and contain only alphanumeric characters.")
        elif len(username) > 10:
            print("Username cannot exceed 10 characters.")
        elif len(password) < 5:
                print("Password cannot exceed 5 characters.")
        else:
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
