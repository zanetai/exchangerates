import requests


def GetAction():
    while True:
        action = input("Do you want to buy or sell currency? For buy press 'b', for sell press 's': ").strip().lower()
        if action == 'b':
            return action
        if action == 's':
            return action
        else:
            print("You have to press 'b' or 's'!")
            continue

def GetCurrency():
    while True:
        currency = input("What currency do you want to buy/sell (ISO STANDARD?): ")
        response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/C/{currency}/')
        if (response.status_code != requests.codes.ok):
            print('Something went wrong! Have you entered the currency in ISO standard?')
            continue
        else:
            return response.json()["rates"][0]["bid"], response.json()["rates"][0]["ask"]


def GetAmount():
    while True:
        try:
            amount = float(input("How much of this currency do you want to buy/sell?: "))
            if amount <= 0:
                print("You can't buy 0 or less!")
                continue
        except ValueError:
            print("You have to type a number!")
            continue
        else:
            return round(amount, 2)


def ChangeJson():
    action = GetAction()
    if action == "s":
        myjson = GetCurrency()
        rate = myjson[0]
        return rate, action
    if action == "b":
        myjson = GetCurrency()
        rate = myjson[1]
        return rate, action

def CountRate(results, amount):
    money = round(results[0] * amount, 2)
    return money

def Main():
    results = ChangeJson()
    amount = GetAmount()
    money = CountRate(results, amount)
    if results[1] == 'b':
        print(f'You will pay {money} PLN')
    if results[1] == 's':
        print(f'You will receive {money} PLN')

if __name__ == "__main__":
    Main()