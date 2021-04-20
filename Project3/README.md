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
Enter the grades of the students: 10
Do you want to continue entering grades? : yes
Enter the grades of the students: 20
Do you want to continue entering grades? : yes
Enter the grades of the students: 35
Do you want to continue entering grades? : yes
Enter the grades of the students: 55
Do you want to continue entering grades? : yes
Enter the grades of the students: 55
Do you want to continue entering grades? : yes
Enter the grades of the students: 100
Do you want to continue entering grades? : yes
Enter the grades of the students: 99
Do you want to continue entering grades? : 88
Enter the grades of the students: 35
Do you want to continue entering grades? : yes
Enter the grades of the students: 50
Do you want to continue entering grades? : No
```

Example graph that will be plotted


![image](https://user-images.githubusercontent.com/77366582/111070336-b53cd600-84a7-11eb-8a9d-0dd842711208.png)


### Error Handling

The program is intended take in integer only. Any attempt to type any other data type is not taken
```bash
Enter the grades of the students: asd
Please enter an integer value: 
35
```
