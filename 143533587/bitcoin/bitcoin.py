import sys, requests, json

def layout(price):
    price = round(price , 4)
    counter =5
    price = str(price)
    new_price = ""
    for i in range(len(price)-1,-1,-1):
        if price[i]==".":
            counter = 0
            new_price+=price[i]
        elif counter == 3:
            new_price += ","+ price[i]
            counter = 1
        else:
            new_price += price[i]
            counter+=1
    price = ""
    for i in range (len(new_price)-1,-1,-1):
        price+= new_price[i]
    return(price)


#checks for command line argument
if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    price = response["bpi"]["USD"]["rate_float"]
    print(price)
    price = layout(price * amount)
    print(f"${price}")
    #print(json.dumps(response.json(), indent =2))

except requests.RequestException:
    pass