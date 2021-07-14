a = input('Enter your score: ')
gemsu = float(a)

def computegrade(gemsu):
    if gemsu>= 0.9 and gemsu<1.0:
        print('A')
    elif gemsu>= 0.8 and gemsu<0.9:
        print('B')
    elif gemsu>= 0.7 and gemsu<0.8:
        print('C')
    elif gemsu>= 0.6 and gemsu<0.7:
        print('D')
    elif gemsu<0.6:
        print('F')
    else:
        print('Bad score')

computegrade(gemsu)
