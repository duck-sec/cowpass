import sys
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



def cowsay(message):
    # Define the cow's speech bubble border
    border = "+" + "-" * (len(message) + 2) + "+"

    # Create the cow's speech bubble
    speech = f"| {message} |"


    # Deploy bovine context
    thought = """
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||
    """

    # Print it.
    print(border)
    print(speech)
    print(border)
    print(thought)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: cowpass <password_length>")
    else:
        password_length = int(sys.argv[1])
        if password_length <= 0:
            print("Password length must be a positive integer.")
        else:
            random_password = generate_password(password_length)
            cowsay(random_password)