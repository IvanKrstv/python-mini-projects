import re

class Validator:

    @staticmethod
    def find_email(text: str) -> list or int:
        """
        This function finds and returns a list with all email addresses from the given text.
        """

        pattern = r'\b[A-Za-z0-9-\._]+[a-z0-9]+@[a-z0-9-\.]+\.[a-z]{2,}\b' # Regex pattern

        match = re.search(pattern, text) # Checks for valid email

        if match:
            return re.findall(pattern, text)
        else:
            return -1

    @staticmethod
    def extract_emails_and_phones(text: str) -> tuple:
        """
        This function finds and returns all email addresses and phone numbers from the given text.
        """

        pattern_phone = r'\+\d+( |-)\d+\1\d+\1\d+\b' # Regex pattern

        emails = Validator.find_email(text) # Find all emails in the text

        if re.search(pattern_phone, text): # Check for valid phone numbers
            phone_numbers = [number.group() for number in re.finditer(pattern_phone, text)] # Find all phone numbers in the text
        else:
            phone_numbers = -1

        return emails, phone_numbers

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        This function checks if the given email is valid.
        """

        pattern = r'\b[A-Za-z0-9-\._]+[a-z0-9]+@[a-z0-9-\.]+\.[a-z]{2,}\b' # Regex pattern

        match = re.match(pattern, email) # Check if the email format is valid
        if match:
            return True
        else:
            return False

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        This function checks if the given password is strong.
        """

        pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}' # Regex pattern

        match = re.match(pattern, password) # Check if the password is strong enough
        if match:
            return True
        else:
            return False
