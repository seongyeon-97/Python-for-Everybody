ratstr=input('Enter a number: ')
try:
    ival=int(ratstr)
except:
    ival=-1
if ival>0:
    print('Nice work')
else:
    print('Not a number')
