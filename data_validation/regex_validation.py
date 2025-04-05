import re

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

def extract_emails_and_phones(text: str) -> tuple or int:
    """
    This function finds and returns all email addresses and phone numbers from the given text.
    """
    # Regex patterns
    pattern_email = r'\b[A-Za-z0-9-\._]+[a-z0-9]+@[a-z0-9-\.]+\.[a-z]{2,}\b'
    pattern_phone = r''

    # Find all emails in the text

    # Find all phone numbers in the text

    # Return both lists (emails, phones)