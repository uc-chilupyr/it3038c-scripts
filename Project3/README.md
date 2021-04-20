# Project 3

### Instructions to run this program 

This program takes the input of from the User and coverts the entered currency into a desired currency.

To run this program, make sure that Python3 is installed and working. You can validate this by running in your command prompt on Windows or Linux:

If using Windows, type:
```powershell
python --version
```

If using Linux, you may need to specify Python3
```bash
python3 --version
```

Now, from the Project1 folder that contains main.py, run the program using Python

```bash
python3 main.py
```

Before running it is important to install the requried module for the API requests and for BeautifulSoup which I used for the data.

So to install type the following 
```bash
python -m pip install bs4 requests 
```

If python isn't install on your windows system you can type
```bash
D:\ python
```
to install it from mircrosoft store

if you are using pycharm or any other IDE to test you can directly install it on the IDE

Example Output: 
```bash
$ python3 main.py
What would you like to do? (Enter help to look at the coversion codes or Enter convert to using the conversion scale): 
Enter the currency to be converted from:: USD
Enter the currency to be converted to:: EUR
How much: 200
200 USD = 166.15 EUR

Process finished with exit code 0
```

There is a help table with the country codes and their names in the code. Just type 'HELP' to see it.
Here is an example of that output.
```bash
$ python3 main.py
                                            Name Code
0                    United Arab Emirates Dirham  AED
1                            Afghanistan Afghani  AFN
2                                    Albania Lek  ALL
3                                   Armenia Dram  AMD
4                   Netherlands Antilles Guilder  ANG
..                                           ...  ...
157  Comptoirs Français du Pacifique (CFP) Franc  XOF
158                                   Yemen Rial  XPF
159                            South Africa Rand  YER
160                                Zambia Kwacha  ZAR
161                              Zimbabwe Dollar  ZMW

[162 rows x 2 columns]

Process finished with exit code 0
```


### Error Handling

The program is inteneded to take valid currency codes as inputs for the currencies. Any attempt to type any other data type is not taken
```bash
$ python3 main.py
What would you like to do? (Enter help to look at the coversion codes or Enter convert to using the conversion scale): 
Enter the currency to be converted from:: sadasf
Please enter a valid currency: 
Enter the currency to be converted from:: USD
Enter the currency to be converted to:: fasf
Please enter a valid currency: 
Enter the currency to be converted to:: INR
How much: 200
200 USD = 15089.61 INR

Process finished with exit code 0
```

Thank you taking the time to look at my work.

I used https://fixer.io/documentation and https://discord.com/channels/@me/434789406918836224/834193124128456717 for reference in my project.
