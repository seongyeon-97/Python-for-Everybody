hor = input('Enter Hour: ')
rat = input('Enter Rate: ')
try:
    hour = float(hor)
    rate = float(rat)
except:
    print('Error, please enter numeric input')
    quit()

if hour>40:
    pay = hour * rate
    more = (hour-40) * (rate*0.5)
    hap = pay + more
else:
    hap = hour * rate
print('Pay:', hap)
