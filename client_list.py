from dataclasses import replace


def main():
    
    infile = open('clients.txt','r')

    i = 0
    for row in infile:
        i+=1
        print(i,'. ',row.rstrip('\n'),sep = '')

main()