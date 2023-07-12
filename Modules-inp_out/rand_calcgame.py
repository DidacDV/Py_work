from random import randint
from string import digits

def main():
    announce()
    digits = get_n_digits()
    total = 0
    i = 0
    while i < 10:
        x = generate_integer(digits)
        y = generate_integer(digits)
        correct = False
        j = 0
        while not correct and j < 3:
            print(f"{x} + {y} = ", end = '')
            try:
                result = int(input())
                if result != x + y:
                    j += 1
                    if j != 3:
                        print(f"ERROR, you have {3-j} tries left")
                else:
                    total += 1
                    correct = True
            except ValueError:
                j += 1
                if j != 3:
                    print(f"ERROR, you have {3-j} tries left")
            if j == 3:
                print(f"ERROR, correct solution is: {x + y}")
        i += 1
    print(f"Score: {total}")
def get_n_digits():
    while True:
        try:
            n = int(input("Digits: "))
            if n > 0 and n < 4:
                return n
        except ValueError:
            pass

def announce():
    print(f"Welcome, you will be given 10 operations of n digits of your choice (n > 0 and n < 4). When no more operations are left, your score will be printed.\nYou have 3 tries per operation.")
def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)

if __name__ == "__main__":
    main()