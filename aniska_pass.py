# -*- coding: utf-8 -*- 
# This line specifies that the file uses UTF-8 encoding. It is necessary for handling non-ASCII characters like emojis.
# UTF-8 is capable of encoding all possible characters (Unicode), ensuring that emojis and special characters are correctly interpreted.

import random  # Import the random module for selecting random characters from character sets.
import string  # Import the string module for accessing sets of characters like uppercase, lowercase, digits, etc.
import argparse  # Import the argparse module for parsing command-line arguments.

# Define the PasswordGenerator class that generates passwords.
class PasswordGenerator:
    # Constructor: Initializes the password generator with various options and limits for characters.
    def __init__(self, length=12, uppercase=True, lowercase=True, digits=True, special=True, emojis=True, 
                 max_uppercase=None, max_lowercase=None, max_digits=None, max_special=None, max_emojis=None, unicode_emojis=False):
        # Initializing instance variables with user input or default values
        self.length = length  # Password length
        self.uppercase = uppercase  # Whether to include uppercase letters
        self.lowercase = lowercase  # Whether to include lowercase letters
        self.digits = digits  # Whether to include digits
        self.special = special  # Whether to include special characters
        self.emojis = emojis  # Whether to include emojis
        self.max_uppercase = max_uppercase  # Maximum number of uppercase letters allowed
        self.max_lowercase = max_lowercase  # Maximum number of lowercase letters allowed
        self.max_digits = max_digits  # Maximum number of digits allowed
        self.max_special = max_special  # Maximum number of special characters allowed
        self.max_emojis = max_emojis  # Maximum number of emojis allowed
        self.unicode_emojis = unicode_emojis  # Whether to return Unicode representations for emojis

    # Main method that generates the password based on selected character sets
    def generate_password(self):
        character_pool = []  # List to hold all possible characters for the password
        password = []  # List to store the generated password characters

        # Helper function to select random characters from a given set up to the maximum allowed count
        def add_characters(char_set, max_count):
            # Randomly choose characters from char_set if max_count is specified, otherwise use the entire set
            return [random.choice(char_set) for _ in range(max_count)] if max_count is not None else list(char_set)

        # Adding uppercase letters to the character pool if selected
        if self.uppercase:
            # Generate uppercase characters up to max_uppercase, or include all if no max is set
            uppercase_chars = add_characters(string.ascii_uppercase, self.max_uppercase or self.length)
            character_pool.extend(uppercase_chars)  # Add to the character pool

        # Adding lowercase letters to the character pool if selected
        if self.lowercase:
            # Generate lowercase characters up to max_lowercase, or include all if no max is set
            lowercase_chars = add_characters(string.ascii_lowercase, self.max_lowercase or self.length)
            character_pool.extend(lowercase_chars)  # Add to the character pool

        # Adding digits to the character pool if selected
        if self.digits:
            # Generate digits up to max_digits, or include all if no max is set
            digit_chars = add_characters(string.digits, self.max_digits or self.length)
            character_pool.extend(digit_chars)  # Add to the character pool

        # Adding special characters to the character pool if selected
        if self.special:
            # Generate special characters up to max_special, or include all if no max is set
            special_chars = add_characters(string.punctuation, self.max_special or self.length)
            character_pool.extend(special_chars)  # Add to the character pool

        # Adding emojis or their Unicode representations to the character pool if selected
        if self.emojis:
            # A string containing all available emojis to use in the password , a total of 158 emojis are used here
            emoji_str = "😂❤️🤣👍😭🙏😘🥰😍😊🎉😁💕🥺😅🔥🤦♥️🤷🙄😆🤗😉🎂🤔👏🙂😳🥳😎👌💜😔💪✨💖👀😋😏😢👉💗😩💯🌹💞🎈💙😃😡💐😜🙈🤞😄🤤🙌🤪❣️😀💀👇💔😌💓🤩🙃😬😱😴🤭😐🌞😒😇🌸😈✌️🎊🥵😞💚☀️💰😚👑🎁💥🙋☹️😑🥴👈💩✅👋🤮😤🤢🌟😥🌈💛😝😫😲‼️🔴🌻🤯💃👊🤬🏃😕👁️⚡☕🍀💦⭐🦋🤨🌺😹🤘🌷💝💤🤝🐰😓💘🍻😟😣🧐😠🤠😻🌙😛🤙🙊"
            
            # If unicode_emojis is True, convert emojis to Unicode representation
            if self.unicode_emojis:
                # Randomly choose emojis and convert them to Unicode (e.g., U+1F602 for 😂) --> each unicode for each emoji consists of 7 bits
                emoji_chars = [f"U+{ord(emoji):X}" for emoji in random.sample(emoji_str, min(self.max_emojis or self.length, len(emoji_str)))]
            else:
                # Add actual emojis if unicode_emojis is False
                emoji_chars = add_characters(emoji_str, self.max_emojis or self.length)
            
            character_pool.extend(emoji_chars)  # Add to the character pool

        # Ensure at least one character set is selected, otherwise raise an error
        if not character_pool:
            raise ValueError("At least one character set must be selected")

        # Randomly select characters from the pool until the password reaches the specified length
        while len(password) < self.length:
            password.append(random.choice(character_pool))  # Append random characters to the password list

        # Join the list of characters into a single string for the final password
        password_str = ''.join(password)
        print("Your Password:", password_str)  # Print the generated password
        return password_str  # Return the generated password string

# Main function that sets up the command-line interface (CLI) for the password generator
def main():
    # argparse helps parse command-line arguments for customization
    parser = argparse.ArgumentParser(description='Password generator with optional emoji Unicode output')

    # Add argument for password length
    parser.add_argument('length', type=int, default=12, help='Length of password')

    # Optional flags to include specific character sets
    parser.add_argument('-u', '--uppercase', action='store_true', help="Include uppercase letters")
    parser.add_argument('-l', '--lowercase', action='store_true', help="Include lowercase letters")
    parser.add_argument('-d', '--digits', action='store_true', help="Include digits")
    parser.add_argument('-s', '--special', action='store_true', help="Include special characters")
    parser.add_argument('-e', '--emojis', action='store_true', help="Include emojis")
    
    # Optional arguments for limiting the number of characters in each set
    parser.add_argument('-mu', '--max_uppercase', type=int, default=None, help="Maximum number of uppercase characters")
    parser.add_argument('-ml', '--max_lowercase', type=int, default=None, help="Maximum number of lowercase characters")
    parser.add_argument('-md', '--max_digits', type=int, default=None, help="Maximum number of digits")
    parser.add_argument('-ms', '--max_special', type=int, default=None, help="Maximum number of special characters")
    parser.add_argument('-me', '--max_emojis', type=int, default=None, help="Maximum number of emojis")
    
    # Flag to generate Unicode representations of emojis
    parser.add_argument('--unicode-emojis', action='store_true', help="Output Unicode values for emojis")

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Create an instance of PasswordGenerator with the parsed arguments
    password_generator = PasswordGenerator(args.length, args.uppercase, args.lowercase, args.digits, args.special, args.emojis,
                                           args.max_uppercase, args.max_lowercase, args.max_digits, args.max_special, args.max_emojis,
                                           args.unicode_emojis)
    
    # Call the password generator to create the password
    password_generator.generate_password()

# If the script is executed directly, call the main() function
if __name__ == "__main__":
    main()  
