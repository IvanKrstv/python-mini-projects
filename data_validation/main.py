from regex_validation import Validator

def menu():
    print("Python Validator ✅\n"
          "\n1️⃣. Find emails"
          "\n2️⃣. Extract emails and phone numbers"
          "\n3️⃣. Validate email"
          "\n4️⃣. Validate password"
          "\n5️⃣. Extract dates"
          "\n6️⃣. Extract links"
          "\n7️⃣. Replace words"
          "\n8️⃣. Exit")
    choice = input("\nEnter your choice: ")

    return choice

def main():
    while True:
        choice = menu()
        text = input("Enter your text: ")
        print()

        if choice == '1':
            emails = Validator.find_email(text) # List of emails if there are any
            if emails == -1: # No emails
                print("No emails were found in the text.")
            else: # There are emails
                print(f"Emails: {', '.join(emails)}")

        elif choice == '2':
            emails, phone_numbers = Validator.extract_emails_and_phones(text) # Unpack emails and phone numbers lists
            if emails == -1: # No emails
                print("No emails were found in the text.")
            else: # There are emails
                print(f"Emails: {', '.join(emails)}")
            if phone_numbers == -1: # No phone numbers
                print("No phone numbers were found in the text.")
            else: # There are phone numbers
                print(f"Phone numbers: {', '.join(phone_numbers)}")

        elif choice == '3':
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '6':
            pass

        elif choice == '7':
            pass

        elif choice == '8':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8!\n")
            continue

if __name__ == '__main__':
    main()