from donations_pkg.homepage import show_homepage

def login(database, username, password):
    username = username.lower()
    if username in [key.lower() for key in database]:
        if database[[key for key in database if key.lower() == username][0]] == password:
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

def register(database, username):
    username = username.lower()
    if username in [key.lower() for key in database]:
        print("Username already exists")
        return ""
    else:
        print(f"Username {username} has been registered!")
        return username