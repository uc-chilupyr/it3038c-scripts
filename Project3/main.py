import requests
import pandas as pd
from bs4 import BeautifulSoup as bs


#get the code_name data from the website
def get_code():
    link = 'https://www.xe.com/iso4217.php'
    r = requests.get(link)
    soup = bs(r.content, 'html.parser')
    codes = []
    names = []
    tables = soup.findAll('table', {'class': 'sPg_tbl'})
    for table in tables:
        symbols = table.findAll('a')
        for symbol in symbols:
            codes.append(symbol.text)

    for table in tables:
        symbols = table.findAll('td', {'class': 'tblBrdrLn'})
        for symbol in symbols:
            names.append(symbol.text)

    del names[0::2]
    df = pd.DataFrame(list(zip(names, codes)), columns=["Name", "Code"])
    return df

#coverts the desired currency to EURO since that is what is used by the API

def converter(url, currency1, currency2, value):
    data = requests.get(url).json()
    conversion_rates = data['rates']
    amount = float(value)

    if currency1 != 'EUR':
        Euro_amount = amount / float(conversion_rates[currency1])

    c2_amount = round(Euro_amount * conversion_rates[currency2], 2)

    print(str(value) + ' ' + str(currency1) + ' = ' + str(c2_amount) + ' ' + str(currency2))


if __name__ == '__main__':

    url = 'http://data.fixer.io/api/latest?access_key=3a27a3c2e4c7804b57dbffc707d4b7de'

    prompt = input(
        'What would you like to do? (Enter help to look at the coversion codes or Enter convert to using the conversion scale): ')
    if (prompt.upper() == 'HELP'):
        print(get_code())
    else:
        currency1 = input('Enter the currency to be converted from: ').upper()
        currency2 = input('Enter the currency to be converted to:: ').upper()
        value = input('How much: ')

        while (1):
            if (currency1 == 'HELP' or currency2 == 'HELP'):
                print(get_code())
                currency1 = input('Enter the currency to be converted from: ').upper()
                currency2 = input('Enter the currency to be converted to: ').upper()

                value = input('How much: ')
            elif (currency1 not in get_code() or currency2 not in get_code()):
                print('Enter a valid currency: ')
                currency_name = ['US dollar', 'Indian Rupee', 'British Pound', 'Euro']
                currency1 = input('Enter the currency to be converted from:: ').upper()
                currency2 = input('Enter the currency to be converted to:: ').upper()
                value = input('How much: ')
                break
        converter(url, currency1, currency2, value)
