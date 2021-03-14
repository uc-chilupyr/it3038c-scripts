# Project 2

### Instructions to run this program 

This program takes the input of Student grades from the user and plots a graph showing the number of students and thier respectives scores.

The number of students dependes on the number of grades entered as the program works on the logic that each student has a unique score.

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

Before running it is important to install the requried module so that a graph can be plotted.

So to install type the following 
```bash
python -m pip install -U pip
python -m pip install -U matplotlib
```

If python isn't install on your windows system you can type
```bash
D:\ python
```
to install it from mircrosoft store

If you are on Linux, you might prefer to use your package manager. Matplotlib is packaged for almost every major Linux distribution.
```bash

    Debian / Ubuntu: sudo apt-get install python3-matplotlib
    Fedora: sudo dnf install python3-matplotlib
    Red Hat: sudo yum install python3-matplotlib
    Arch: sudo pacman -S python-matplotlib

```
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

Thank you for taking your time to go through my project.
