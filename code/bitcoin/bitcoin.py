import sys
import requests
import json
try:
    n = sys.argv[1]
    try:
        n = float(n)
    except ValueError:
        sys.exit("Command-line argument is not an number")
except:
    sys.exit("Missing command-line argument")



response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
info = json.dumps(data, indent = 4)
json_load = (json.loads(info))
rate = ((json_load["bpi"]["USD"]["rate_float"]))

amount = (rate*n)
print(f"${amount:,.4f}")



