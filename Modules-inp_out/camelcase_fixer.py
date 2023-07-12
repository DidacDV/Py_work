import sys


def convertcamel(word):
    new = ""
    for c in word:
        if c.isupper():
            new += '_' + c.lower()
        else:
            new += c
    return new


def main():
    result = ''
    try:
        with open("result.txt", "w") as res:
            with open(sys.argv[1]) as fitxer:
                for line in fitxer:
                    for word in line:
                        res.write(convertcamel(word))

    except IndexError:
        print("Insert file name")


if __name__ == "__main__":
    main()