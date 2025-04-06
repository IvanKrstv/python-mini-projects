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
    print()

    return choice


def main():
    while True:
        choice = menu()
        if choice in ('1', '2', '5', '6', '7'):
            text = input("Enter your text: ")
            print()

        if choice == '1':
            emails = Validator.find_email(text)  # List of emails if there are any
            if emails == -1:  # No emails
                print("No emails were found in the text.")
            else:  # There are emails
                print(f"Emails: {', '.join(emails)}")

        elif choice == '2':
            emails, phone_numbers = Validator.extract_emails_and_phones(text)  # Unpack emails and phone numbers lists
            if emails == -1:  # No emails
                print("No emails were found in the text.")
            else:  # There are emails
                print(f"Emails: {', '.join(emails)}")
            if phone_numbers == -1:  # No phone numbers
                print("No phone numbers were found in the text.")
            else:  # There are phone numbers
                print(f"Phone numbers: {', '.join(phone_numbers)}")

        elif choice == '3':
            email = input("Enter email: ")
            print()
            if Validator.validate_email(email):
                print(f"The email {email} is valid.")
            else:
                print(f"The email {email} is not valid.")

        elif choice == '4':
            password = input("Enter password: ")
            print()
            if Validator.validate_password(password):
                print(f"The password is valid.")
            else:
                print(f"The password is not valid.")

        elif choice == '5':
            dates = Validator.extract_dates(text)
            if dates:
                print(f"Dates: {'; '.join(dates)}.")
            else:
                print("No dates in format DD/MM/YYYY or MM-DD-YYYY were found.")

        elif choice == '6':
            links = Validator.extract_links(text)
            if links:
                print(f"URLs: {'; '.join(links)}")
            else:
                print("No links were found in the text.")

        elif choice == '7':
            old_word = input("Enter word to be replaced in the text: ")
            new_word = input("Enter replacement: ")
            new_text = Validator.replace_word(text, old_word, new_word)
            print(new_text)

        elif choice == '8':
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 8!\n")
            continue


if __name__ == '__main__':
    main()
