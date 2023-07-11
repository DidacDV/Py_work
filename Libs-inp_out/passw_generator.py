import random
import string

def generate_password(lp, ch):
    return ''.join(random.choice(ch) for i in range(lp))


def main():
    while True:
        try :
            lenght_pass = int(input("Insert the desired lenght of the password: "))
            break
        except ValueError:
            print("Insert integer")
    choices = string.ascii_letters + string.digits                                       
    question = input("Do you want special characters? ")
    if question.lower() == "yes":
        choices += "~`! @#$%^&*()_-+={[}]|\:;<,>.?/"
    passw = generate_password(lenght_pass, choices)
    print(f"Password generated: {passw}")

if __name__ == "__main__":
    main()