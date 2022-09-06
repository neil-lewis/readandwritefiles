import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)

for row in csvfile:
    print('ID:', row[0])
    print('Name:', row[1], row[2])
    print('Salary:', row[3])
    print('Bonus: ', float(row[4]) * 100, '%', sep = '')
    salary = (float(row[3]) * float(row[4])) + float(row[3])
    print('Total Pay: ', '$' ,format(salary,',.2f'), sep = '')
    input('Press enter to continue')