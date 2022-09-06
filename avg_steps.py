import csv

infile = open('steps.csv', 'r')

csvfile = csv.reader(infile, delimiter = ',')

outfile = open('avg_steps.csv', 'w')

jan = 0
jan_cnt = 0
feb = 0
feb_cnt = 0
mar = 0
mar_cnt = 0
apr = 0
apr_cnt = 0
may = 0
may_cnt = 0
jun = 0
jun_cnt = 0
jul = 0
jul_cnt = 0
aug = 0
aug_cnt = 0
sep = 0
sep_cnt = 0
ocb = 0
ocb_cnt = 0
nov = 0
nov_cnt = 0
dec = 0
dec_cnt = 0

for row in csvfile:
    if row[0] == '1':
        jan += int(row[1])
        jan_cnt += 1
    elif row[0] == '2':
        feb += int(row[1])
        feb_cnt += 1
    elif row[0] == '3':
        mar += int(row[1])
        mar_cnt += 1
    elif row[0] == '4':
        apr += int(row[1])
        apr_cnt += 1
    elif row[0] == '5':
        may += int(row[1])
        may_cnt += 1
    elif row[0] == '6':
        jun += int(row[1])
        jun_cnt += 1
    elif row[0] == '7':
        jul += int(row[1])
        jul_cnt += 1
    elif row[0] == '8':
        aug += int(row[1])
        aug_cnt += 1
    elif row[0] == '9':
        sep += int(row[1])
        sep_cnt += 1
    elif row[0] == '10':
        ocb += int(row[1])
        ocb_cnt += 1
    elif row[0] == '11':
        nov += int(row[1])
        nov_cnt += 1
    elif row[0] == '12':
        dec += int(row[1])
        dec_cnt += 1

jan_1 = format(jan / jan_cnt,'.2f')
feb_1 = format(feb / feb_cnt,'.2f')
mar_1 = format(mar / mar_cnt,'.2f')
apr_1 = format(apr / apr_cnt,'.2f')
may_1 = format(may / may_cnt,'.2f')
jun_1 = format(jun / jun_cnt,'.2f')
jul_1 = format(jul / jul_cnt,'.2f')
aug_1 = format(aug / aug_cnt,'.2f')
sep_1 = format(sep / sep_cnt,'.2f')
ocb_1 = format(ocb / ocb_cnt,'.2f')
nov_1 = format(nov / nov_cnt,'.2f')
dec_1 = format(dec / dec_cnt,'.2f')

outfile.write('January, ')
outfile.write(str(jan_1))
outfile.write('\n')
outfile.write('February, ')
outfile.write(str(feb_1))
outfile.write('\n')
outfile.write('March, ')
outfile.write(str(mar_1))
outfile.write('\n')
outfile.write('April, ')
outfile.write(str(apr_1))
outfile.write('\n')
outfile.write('May, ')
outfile.write(str(may_1))
outfile.write('\n')
outfile.write('June, ')
outfile.write(str(jun_1))
outfile.write('\n')
outfile.write('July, ')
outfile.write(str(jul_1))
outfile.write('\n')
outfile.write('August, ')
outfile.write(str(aug_1))
outfile.write('\n')
outfile.write('September, ')
outfile.write(str(sep_1))
outfile.write('\n')
outfile.write('October, ')
outfile.write(str(ocb_1))
outfile.write('\n')
outfile.write('November, ')
outfile.write(str(nov_1))
outfile.write('\n')
outfile.write('December, ')
outfile.write(str(dec_1))

outfile.close()

