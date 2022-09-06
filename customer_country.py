import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile, delimiter = ',')

outfile = open('customer_country.csv', 'w')

next(csvfile)

outfile.write('Full Name, Country\n')

for row in csvfile:
    outfile.write(row[1] + ' ' + row[2] + ', ' + row[4] +'\n')

outfile.close()

