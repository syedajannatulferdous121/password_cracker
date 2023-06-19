import hashlib
import itertools
import string

def password_cracker(password_hash, password_list):
    for password in password_list:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == password_hash:
            return password
    return None

def generate_password_list(max_length=6):
    password_list = []
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password_list.append("".join(combination))

    return password_list

# Get user input
password_hash = input("Enter the password hash: ")
username = input("Enter the username: ")
link = input("Enter the link: ")

# Generate password list
password_list = generate_password_list(max_length=6)

# Attempt to crack the password
cracked_password = password_cracker(password_hash, password_list)

# Print the result
if cracked_password:
    print(f"Password cracked for {username} on {link}! The password is: {cracked_password}")
else:
    print("Password not found in the given password list.")
