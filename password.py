import random
import string
import json

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to create a new account and generate a password
def create_account(accounts):
    account_name = input("Enter the account name: ")
    password_length = int(input("Enter the desired password length: "))

    if password_length < 8:
        print("Password length must be at least 8 characters.")
        return

    password = generate_password(password_length)
    accounts[account_name] = password
    print(f"Password for '{account_name}' has been generated and saved.")

# Function to view saved account passwords
def view_accounts(accounts):
    if not accounts:
        print("No accounts saved.")
    else:
        print("Saved Accounts:")
        for account, password in accounts.items():
            print(f"{account}: {password}")

# Function to save accounts to a JSON file
def save_to_file(accounts, filename="passwords.json"):
    with open(filename, "w") as file:
        json.dump(accounts, file)
    print(f"Accounts saved to '{filename}'.")

# Function to load accounts from a JSON file
def load_from_file(filename="passwords.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
    accounts = load_from_file()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Create New Account and Generate Password")
        print("2. View Saved Account Passwords")
        print("3. Save Accounts to File")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            view_accounts(accounts)
        elif choice == "3":
            save_to_file(accounts)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("Goodbye!")
