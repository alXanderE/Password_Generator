import random
import string
import os

def generate_password(length=12):
    #Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    if __name__ == "__main__":
        filepath = os.path.join("stored_passwords", "newpassword.txt")
        password_length = int(input("Enter the desired password length: "))

        if password_length < 8:
            print("Password length must be at least 8 character.")
            main()
        else:
            generated_password = generate_password(password_length)
            print("Generated password:", generated_password)
            with open(filepath,'w') as f:
                f.write(generated_password)
            print("password saved in stored_passwords folder")

main()
