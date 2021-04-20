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
    else:
        Euro_amount = amount
    c2_amount = round(Euro_amount * conversion_rates[currency2], 2)

    print(str(value) + ' ' + str(currency1) + ' = ' + str(c2_amount) + ' ' + str(currency2))


if __name__ == '__main__':

    url = 'http://data.fixer.io/api/latest?access_key=3a27a3c2e4c7804b57dbffc707d4b7de'
    codes = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SPL*', 'SRD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', ' BEAC', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWD']
    prompt = input('What would you like to do? (Enter help to look at the coversion codes or Enter convert to using the conversion scale): ')
    while(1):
        if(prompt.upper() == 'HELP'):
            print(get_code())
        else:
            while(1):
                currency1 = input('Enter the currency to be converted from:: ').upper()
                if(currency1 not in codes):
                    print("Please enter a valid currency: ")
                else:
                    break
            while (1):
                currency2 = input('Enter the currency to be converted to:: ').upper()
                if(currency2 not in codes):
                    print("Please enter a valid currency: ")
                else:
                    break
            value = input('How much: ')
            converter(url, currency1, currency2, value)
            break
    



