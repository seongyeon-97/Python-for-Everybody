str = 'X-DSPAM-Confidence:0.8475'
sval = str.find(':')
#print(sval)
fval = str[sval+1:]
#print(fval)
value = float(fval)
print(value)
