
import random

def generate_password():

    print("=== PRO PASSWORD GENERATOR ===")

    try:
        numbers_count = int(input("Enter number count: "))
        symbols_count = int(input("Enter symbol count: "))
        letters_count = int(input("Enter letter count: "))

        if numbers_count < 0 or symbols_count < 0 or letters_count < 0:
            print("Invalid input (no negative values)")
            return

        password_list = []

        for _ in range(numbers_count):
            password_list.append(str(random.randint(0, 9)))

        for _ in range(symbols_count):
            password_list.append(random.choice("!@#$%^&*"))

        for _ in range(letters_count):
            password_list.append(random.choice("abcdefghijklmnopqrstuvwxyz"))

        random.shuffle(password_list)

        password = "".join(password_list)

        print("\nGenerated Password:")
        print(password)

        if len(password) < 6:
            print("Weak password")
        elif len(password) < 10:
            print("Medium password")
        else:
            print("Strong password")

    except ValueError:
        print("Please enter valid numbers only")

generate_password()
