import random
import string
def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password = random.choice(uppercase_letters)
    password += random.choice(lowercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)
    for _ in range(length - 4):
        password += random.choice(all_characters)
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password you want to generate: "))
    password = generate_password(length)
    print("Generated Password:", password)
