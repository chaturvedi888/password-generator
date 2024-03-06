import random
import string

def generate_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set is included
    password = random.choice(uppercase_letters)
    password += random.choice(lowercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password += random.choice(all_characters)

    # Shuffle the password characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Generated Password:", password)
