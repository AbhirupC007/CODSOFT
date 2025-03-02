import random
import string

def generate_password(length, use_special_chars, special_chars):
    characters = string.ascii_letters + string.digits
    if use_special_chars and special_chars:
        characters += special_chars
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        use_special_chars = input("Do you want special characters? (yes/no): ").strip().lower()
        special_chars = string.punctuation if use_special_chars == "yes" else ""
        
        password = generate_password(length, use_special_chars == "yes", special_chars)
        print(f"Generated Password: {password}")
        
        retry = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()