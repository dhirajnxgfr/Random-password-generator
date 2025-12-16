import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."

    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Random Password Generator")

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
