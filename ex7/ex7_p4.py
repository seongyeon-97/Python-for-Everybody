fname = input('Enter the flie name: ')
try:
    fhand = open(fname)
except:
    print('File cannot opened: ', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('From:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
