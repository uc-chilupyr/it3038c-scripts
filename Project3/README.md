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

Before running it is important to install the requried module for the API requests and for BeautifulSoup

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
![image](https://user-images.githubusercontent.com/77366582/115471234-a44d5600-a205-11eb-8def-717424c67d49.png)

There is a help table with the country codes and their names in the code. Just type 'HELP' to see it.
Here is an example of that output.

![image](https://user-images.githubusercontent.com/77366582/115471694-643aa300-a206-11eb-94ea-95102ce10f46.png)



### Error Handling

The program is inteneded to take valid currency codes as inputs for the currencies. Any attempt to type any other data type is not taken
```bash
Enter the grades of the students: asd
Please enter an integer value: 
35
```
