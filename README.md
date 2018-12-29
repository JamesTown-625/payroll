You are creating part of the payroll program for an Internet electronics store named "FluffShuffle Electronics". The owner of FluffShuffle has given you the following requirements: FluffShuffle employs six (6) people. The owner doesn't expect significant growth in his company, but may grow in the future.  All of the employee data (name, address, etc.) is kept in a text file on your disk. Your program will read this employee data from the file and use that data to calculate the payroll for company employees. The program will have to calculate the payroll deductions for each employee and their net pay.

If you encounter errors while reading a data file, print an error message to the console, and close the file. Your program should not exit, since you might choose another file with correct data.

Suppose that your programming team has come up with a design for this program. In this design the data for each employee on the payroll will be held in a list, a tuple, a dictionary, an object of the Employee class or organized in a dataframe. You get to choose how an employee's data is stored.

An Employee has the following attributes:

1. employee number
2. name
3. street address
4. hourly wage
5. hours worked this week

The Employee as a list or tuple or dict
You can read the data for each employee into a list tuple, or dict, and then store that employee item as one element in the list of employees.

The Employee Class
An employee object will need the following methods:

1. A constructor for the employee class that takes arguments to initialize all of the above mentioned attributes.
2. A method, calc_salary(), that calculates and returns an employee's net pay as a double. 
    An employee's gross pay is calculated by multiplying the hours worked by their hourly wage. Be sure to give time-and-a-half for overtime (anything over 40 hours). To compute the net pay, deduct 20% for Federal income tax, and 7.5% for state income tax.
Every employee on the payroll will need to be represented in the program by its own employee object. A convenient way to handle this will be to create a list of employee objects, using lists, tuples or classes.

Employee as a Row in a DataFrame
You might find it easier to use a pandas dataframe to hold the data in your program.  However,
the data.txt file you downloaded is not a comma-separated file with nice column headings at the top.
You could do this by hand for 6 employees, but not for larger files.  So write a small program that uses
data.txt as input and creates a new file data1.txt.  The new file should have column headings at the top
and each employee's data on a single line after that with each item on a line separated by a comma.  Then you
load the reformatted data and use the dataframe to hold employee data.

GUI
- Your GUI should have a file open and exit navbar selection option. 
- It should three Entry windows labeled "Name" "Address" and "Net Pay"
- Finally it needs to have a next button so that you can see all employees on the payroll.
- You want to add a Previous button (not shown) in order to scroll backward through the data.
