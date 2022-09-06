import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

for row in csvfile:
    print('ID: ', row[0])
    print('Name: ', row[1], row[2])
    print('Salary: ', row[3])
    print('Bonus: ', row[4])
    input('Press enter to continue')