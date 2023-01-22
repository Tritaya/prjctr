# python bank_api.py

import requests
import json
from iso4217 import Currency


def currency_number(name) -> int:
    try:
        return Currency(name.upper()).number
    except ValueError:
        return


def get_response(debug=False) -> [object]:
    if debug:
        with open('dummy.json', encoding='utf-8-sig') as f:
            jsn = json.load(f)
        print('****** DEBUG MODE ********')
        return jsn 
    api_end = 'https://api.monobank.ua/bank/currency'
    try:
        response = requests.get(api_end)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(repr(e))
        print('Something was wrong, please try again later')
        exit()
    jsn = response.json()
    # with open('dummy.json', 'w', encoding='utf-8-sig') as f:
    #     json.dump(jsn, f)
    return response.json()


class Var:
    pass

def get_UA_rate(currency: int, jsn: list) -> tuple:
    Var.ccy = currency
    assert isinstance(currency, int), "Currency must be integer code"
    print(currency, "<- currency number")
    for record in jsn:
        match record:
            case {'currencyCodeA': Var.ccy, 'rateBuy': rate_buy,
                    'currencyCodeB': 980, 'rateSell': rate_sell}:
                # print(record)
                return rate_buy, rate_sell
    print('No info about this currency')
    exit()
            
                

def get_input() -> str:
    def fail_input(x):
        if x == 'UAH':
            print("You must input only foreign currency")
            return True
        print("Invalid input")
        return not bool(currency_number(x.upper()))

    while (
        fail_input(
            x := input("Enter the currency 'USD', 'EUR', 'PLN' or other currency \nwithout quotes (case insensitive): ").upper()
            )):
            continue

    print('You entered', x)
    return x


def output(buy_rate, sell_rate, currency):
    print(f'The information about {currency}:\nthe buy rate --> {buy_rate},\nthe sell rate --> {sell_rate}')


def main():
    # jsn = get_response(debug=True)
    jsn = get_response()
    ccy_string = get_input()
    ccy = currency_number(ccy_string)
    rates = get_UA_rate(currency=ccy, jsn=jsn)
    # print(rates)
    output(*rates, ccy_string)


if __name__ == '__main__':
    main()
