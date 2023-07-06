#Time input must be on HH:MM format, for example = 03:23
def main():
    try:
        time = input("What time is it? ")
        val = convert(time)
        if 6 <= val and val <= 8:
            print("breakfast time")
        elif 13 <= val and val <= 15:
            print("lunch time")
        elif 20 <= val and val <= 22:
            print("dinner time")
        else: print("Not a meal time :(")
    except ValueError:
        print("Input must have HH:MM format")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)/60
    val = hour + minute
    return val
if __name__ == "__main__":
    main()
