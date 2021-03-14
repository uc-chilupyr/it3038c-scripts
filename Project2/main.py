import matplotlib.pyplot as plt # impoty this library to help with plotting graphs


studentGrades = []  # array to store the student grades that are entered

done = False
while not done:  # while loop so that one can keep entering grades

    temp = input("Enter the grades of the students: ")
    try:  # error checking to see if the input is integer or not
        temp1 = int(temp)
    except ValueError:
        while not temp.isdigit():
            print("Please enter an integer value: ")
            temp = input()
            continue
    studentGrades.append(temp)  # adding input to the array
    response = input("Do you want to continue entering grades? : ")
    if response == "No":  # ending while loop if the user response is No
        break
    else:
        continue
studentGrades.sort()  # sorting the grades so that the graph is ordered
noOfStudents = []  # array to hold the number of occurences of grades
for x in studentGrades:
    temp1 = studentGrades.count(x)
    noOfStudents.append(temp1)

plt.bar(studentGrades,noOfStudents)  # plotting a bar graph with Student grades on x-axis and No Of Students get that 
                                        # grade on y-axis 
plt.show()  # to show the graph that is plotted
