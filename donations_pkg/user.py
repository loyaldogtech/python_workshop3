from donations_pkg.homepage import show_homepage

def login(database, username, password):

    if username in database:
        if database[username] == password:
            print(f"\nWelcome back, {username}!\n")
            show_homepage()
            print(f"Logged in as: {username}.")
            return username
        else:
            print("Incorrect password.")
            return ""
    else:
        print("Username not found. Please register.")
        return ""
