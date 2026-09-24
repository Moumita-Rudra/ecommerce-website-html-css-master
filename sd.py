# Simulated user database (in-memory)
user_database = {}

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

def sign_up():
    print("Sign-Up Form")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    email = input("Enter your email: ")

    if username in user_database:
        print("Username already exists. Please choose another one.")
    else:
        user = User(username, password, email)
        user_database[username] = user
        print("Registration successful. You can now log in.")

def main():
    while True:
        print("\nWelcome to the Sign-Up System")
        print("1. Sign up")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
