menu = {
    "Durum Kebab": 4.00,
    "Rice Plate": 5.50,
    "Pita Kebab": 6.50,
    "Mixed Plate 1": 11.00,
    "Mixed Plate 2": 6.50,
    "Mixed Plate 3": 7.00,
    "Menu Pita": 6.00,
    "Menu Durum": 6.50,
    "French Chips": 2.50,
    "Nuggets": 3.50
}

print("Welcome to your local kebab! this is the menu of the day:")
for i in menu:
    print(i, end = ' ')
    print(f"${menu[i]}")
total = 0
while True:
    print("Item: ", end = '')
    try:
        item = input()
        item = item.title()
        try:
            price = menu[item]
            total += price
            print("Total: $" , end="")
            print("{:.2f}".format(total))
        except KeyError:
            print("Item not found, try again")
    except EOFError:
        print("Thanks for coming amigo, bye!")
        break