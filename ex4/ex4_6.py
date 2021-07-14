hor = input('Enter Hour: ')
rat = input('Enter Rate: ')
hour = float(hor)
rate = float(rat)

def computepay(hour, rate):
    print('일 한 시간: ', hour, '시급: ', rate)
    if hour>40:
        pay = hour * rate
        more = (hour-40) * (rate * 0.5)
        hap = pay + more
    else:
        hap = hour * rate
    return(hap)


total = computepay(hour, rate)
print('Pay:', total)
