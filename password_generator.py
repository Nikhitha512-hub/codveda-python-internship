import random
import string

print("=== Password Generator ===")

# User input
length = int(input("Enter password length: "))

# Characters to use in password
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

# Display password
print("\nGenerated Password:")
print(password)