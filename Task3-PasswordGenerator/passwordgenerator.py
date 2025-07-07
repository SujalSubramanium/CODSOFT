import random
import string

def generate_password():
    try:
        length = int(input("Password length: "))
        if length < 4:
            print("Minimum length is 4.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        print("Generated Password:", password)
    except:
        print("Please enter a valid number.")

if __name__ == "__main__":
    generate_password()