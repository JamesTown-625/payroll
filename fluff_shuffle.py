""" 
Author Name: James Teerlink 
Course: CS 1400 Fundamentals of Programming
Project 7: FluffShuffle Electronics Payroll
Due Date: 11/30/2018
No help was used while writing this code

Use the tkinter module to create a GUI application that the 
user can use to view the net pay of each employee at 
FluffShuffle Electronics. The program will read a text file
list of all the employees with their unique information and
calculate their net pay based on their wage and hours worked. 
Program needs to be able to have more than 6 people in the text
file as the company may grow in the future. If user encounters a 
text file error print error to the console and close the file. 

0.  Import the tkinter module and create the GUI, make sure that there is a loop to listen for user events
1.  Create the employee class with a constructor function that initializes employee attributes
2.  Define a function in the employee class that will calculate the net pay of each employee 
3.  Create a temporary dictionary and an employees list to use for organizing the employee data
4.  Define function "data_read" that will read the data from user selected *.txt file and put info in employees list  
5.  Define function "navFunc" that will allow user to click buttons on GUI and go to next and previous employee in the employees list
6.  Create the application GUI window with tkinter
7.  Call the data_read function with filename user chose so that it will read the *.txt file 
8.  Style the window with: title, menubar, 3 entries, and two buttons
9.  Put the application window in a tkinter mainloop to listen for user events
"""

import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog

#Employee class to create new instances of an FluffShuffle Employee
class Employee:
    """ Employee class for representing and manipulating FSE employees info. """
    def __init__(self, eId, eName, eAddress, eWage, eHours):
        """ Create a new employee """
        self.id = eId
        self.name = eName
        self.address = eAddress
        self.wage = eWage
        self.hours = eHours

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getId(self):
        return self.id
    
    def calc_salary(self):
        if float(self.hours) > 40:
            overtime = float(self.hours) - 40
            gross_pay = (40 * float(self.wage)) + (float(self.wage) * overtime * 1.5)
        else:
            gross_pay = float(self.hours) * float(self.wage)

        fed_tax = gross_pay * .20
        state_tax = gross_pay * .075
        net_pay = gross_pay - fed_tax - state_tax
        return net_pay

#Create a temporary dictionary and a employees list for data_read function to store data to
temp_dict = {}
employees = []

# data_read() function opens, reads, and closes the text file
# also organizes the data from text file into an employees list of Employee objects
def data_read(filename):
    inFile = open(filename, 'r')
    message = inFile.readlines()
    start = 0
    stop = 4
    
    arraySize = len(message)//4
    array = []
    for row in message:
        array.append(row.rstrip("\n"))

    for i in range(0, arraySize):
        temp_dict[i] = array[start:stop]
        stop = stop + 4
        start = start + 4 
    
    for key, value in temp_dict.items():
        value[3].split()
        value[0] = Employee(int(value[0]),value[1],value[2], float(value[3].split()[0]), float(value[3].split()[1]))
        employees.append(value[0])
          
    inFile.close()
    
    return employees

# NavFunc takes in the employees list of objects, the next/prev direction in list, 
# and the id of current employee being displayed on tkinter window
def navFunc(employees, direction, id):
    pos = int(id) - 1
    if direction == "next":
        pos = pos + 1
        if pos >= len(employees):
            return 
        else:
            nameText.set(employees[pos].getName())
            addressText.set(employees[pos].getAddress())
            salaryText.set("${:.2f}".format(employees[pos].calc_salary()))
            idText.set(employees[pos].getId())
        
    elif direction == "prev":
        if pos == 0:
            return employees[0]
        else: 
            pos = pos - 1
            nameText.set(employees[pos].getName())
            addressText.set(employees[pos].getAddress())
            salaryText.set("${:.2f}".format(employees[pos].calc_salary()))
            idText.set(employees[pos].getId())
    #return first employee in list at the start of the application
    return employees[0]

""" Create the user interface """
#Create the application window
window = tk.Tk()
window.title("FluffShuffle Electronics Payroll")
#Ask user to select the txt file they want to use for payroll
window.filename = filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("text files", "*.txt"), ("all files","*.*")))
#Call data_read function with the filename that the user chose
data_read(window.filename)

#Create the application menu 
menubar = tk.Menu(window)
window.config(menu=menubar)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=filedialog.askopenfilename)
filemenu.add_command(label="Save", command=filedialog.asksaveasfilename)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Exit", command=window.quit)

#Create window frame to manage label, entry, and button layout
frame1 = ttk.Frame(window)
frame1.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S, padx=75, pady=25)

#Labels for 3 values: Name, Address, and Net Pay
name_label = ttk.Label(frame1, text="Name: ")
name_label.grid(row=4, column=2, pady=15)
address_label = ttk.Label(frame1, text="Address: ")
address_label.grid(row=6, column=2, pady=15)
salary_label = ttk.Label(frame1, text="Net Pay: ")
salary_label.grid(row=8, column=3, pady=15)

#Entry fields for 3 values: Name, Address, and Net Pay
#Name Entry
nameText = tk.StringVar()
name = tk.Entry(frame1,textvariable=nameText, state="readonly")
nameText.set(navFunc(employees, "first", employees[0].getId()).getName())
name.grid(row=4, column=3, columnspan=2, sticky=tk.E + tk.W)
#Address Entry
addressText = tk.StringVar()
address = tk.Entry(frame1, textvariable=addressText, state="readonly")
addressText.set(navFunc(employees, "first", employees[0].getId()).getAddress())
address.grid(row=6, column=3, columnspan=2, sticky=tk.E + tk.W)
#Salary Entry
salaryText = tk.StringVar()
salary = tk.Entry(frame1, textvariable=salaryText, state="readonly")
salaryText.set("${:.2f}".format(navFunc(employees, "first", employees[0].getId()).calc_salary()))
salary.grid(row=8, column=4, sticky=tk.E)
#Next Button
next_button = tk.Button(frame1, text="Next", command= lambda: navFunc(employees, "next", idText.get()))
next_button.grid(row=10, column=4, columnspan=2, sticky=tk.E + tk.W, pady=(40,10))
#Prev Button
next_button = tk.Button(frame1, text="Previous", command= lambda: navFunc(employees, "prev", idText.get()))
next_button.grid(row=10, column=2, columnspan=2, sticky=tk.E + tk.W, pady=(40,10))

#Id entry field to show the current employee id and to get the order to pass as the third argument to the
#navFunc function so that user can click "next" and "previous"
idText = tk.StringVar()
id = tk.Entry(window,textvariable=idText, state="readonly", width=2)
idText.set(navFunc(employees, "first", employees[0].getId()).getId())
id.grid(row=1, column=1, padx=0)

#Use tkinter mainloop function to have GUI wait for user interaction
window.mainloop()

