def show_homepage():
    
    print("      === DonateMe Homepage ===     ")
    print("-----------------------------------------")
    print("| 1.   Login     | 2.   Register        |")
    print("-----------------------------------------")
    print("| 3.   Donate    | 4.   Show Donations  |")
    print("-----------------------------------------")
    print("|        5.   Exit                      |")
    print("-----------------------------------------")

def donate(username):
    while True:
        donation_amt = input("Enter amount to donate: ")
        try:
            donation_amt = float(donation_amt)
            if donation_amt > 0:
                donation_string = f"{username} donated ${donation_amt}"
                print("Thank you for your donation!")
                return donation_string
            else:
                print("Donation amount must be positive. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number. Try again.")

def show_donations(donations):
    if len(donations) == 0:
        print("Currently, there are no donations.")
    else:
        total_donations = 0
        for d in donations:
            parts = d.split()
            amount = float(parts[2][1:])  # extract the amount from the string
            total_donations += amount
            print(d)
        print(f"Total donations: ${total_donations:.2f}")
