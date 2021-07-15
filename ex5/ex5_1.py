num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        sval = float(sval)
    except:
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + sval

print(num, tot, tot/num)
