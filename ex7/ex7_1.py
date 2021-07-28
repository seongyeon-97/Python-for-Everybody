fname = input('Enter the flie name: ')
fhand = open(fname)
for line in fhand:
    line = line.upper()
    print(line)
