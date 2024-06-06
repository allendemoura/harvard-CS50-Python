import sys, requests, json

if len(sys.argv) != 2:
    sys.exit("specify number of bitcoins with command line arg")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("incorrect argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
except requests.RequestException:
    sys.exit("Request Exception Error")

price = o["bpi"]["USD"]["rate_float"]

print(f"${price*n:,.4f}")