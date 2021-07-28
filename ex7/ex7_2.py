fname = input('Enter flie name: ')
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    position = line.find(':')
    linenumber = line[20:]
    fval = float(linenumber)
    total = total + fval
    count = count + 1
print('Average spam confidence:', total/count)
