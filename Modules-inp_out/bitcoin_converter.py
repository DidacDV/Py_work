import requests
import sys
if len(sys.argv) < 2:                               #checks if a number was given
    sys.exit("Missing command-line argument")

try:
    coins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    val = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    val = val.json()
    conversion = val["bpi"]["USD"]["rate_float"]
    total = conversion * coins
    print(f"${total:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)