largest = None
smallest = None
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval=int(sval)
    except:
        print('Invalid input')
        continue

    if largest is None or fval>largest:
        largest = fval

    if smallest is None or fval<smallest:
        smallest = fval

print('Maximum is', largest)
print('Minimum is', smallest)
