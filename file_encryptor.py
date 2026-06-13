# Encryption function
def encrypt(text, shift):
    encrypted_text = ""

    for char in text:

        if char.isalpha():

            # Handle uppercase letters
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

            # Handle lowercase letters
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted_text += char

    return encrypted_text


# Decryption function
def decrypt(text, shift):
    decrypted_text = ""

    for char in text:

        if char.isalpha():

            # Handle uppercase letters
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

            # Handle lowercase letters
            else:
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += char

    return decrypted_text


try:
    # Read original file
    file = open("message.txt", "r")
    content = file.read()
    file.close()

    print("Original Text:")
    print(content)

    shift = 3

    # Encrypt
    encrypted = encrypt(content, shift)

    encrypted_file = open("encrypted.txt", "w")
    encrypted_file.write(encrypted)
    encrypted_file.close()

    print("\nEncrypted Text:")
    print(encrypted)

    # Decrypt
    decrypted = decrypt(encrypted, shift)

    decrypted_file = open("decrypted.txt", "w")
    decrypted_file.write(decrypted)
    decrypted_file.close()

    print("\nDecrypted Text:")
    print(decrypted)

except FileNotFoundError:
    print("File not found.")