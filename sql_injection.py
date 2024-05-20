import re
# email validation
def check_input_is_email(input_str):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    #r before the string denotes a raw string, which is often used with regular expressions to avoid unintended escape sequences.
    #^ asserts the start of the string.
    #[\w\.-]+ matches one or more word characters (\w), dots (.), or dashes (-). This part matches the local part of the email address before the "@" symbol.
    #@ matches the "@" symbol literally.
    #[a-zA-Z0-9-]+ matches one or more letters (both uppercase and lowercase), digits, or dashes in the domain part of the email address.
    #\. matches the dot (.) literally. It's escaped with a backslash because dot is a special character in regular expressions and needs to be escaped to be treated as a literal dot.
    #[a-zA-Z]{2,} matches two or more letters (both uppercase and lowercase) in the top-level domain (TLD) part of the email address.
    #$ asserts the end of the string.
    
    # Check if the input string matches the email pattern
    return re.match(email_pattern, input_str) is not None

# Example usage:
user_input = input("Enter an email address: ")
if check_input_is_email(user_input):
    print("Input is a valid email address.")
else:
    print("Input is not a valid email address.")


# empty input validation
def check_input_is_empty(input_str2):
    return len(input_str2.strip()) == 0

# Example usage:
user_input2 = input("Enter something: ")
if check_input_is_empty(user_input2):
    print("Input is empty.")
else:
    print("Input is not empty.")