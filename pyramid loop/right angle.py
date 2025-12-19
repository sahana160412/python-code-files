print(' half pyramid of stars :')
tr=int(input('enter the number of rows:'))
for r in range(1,tr+1):
    for i in range(r):
        print('*', end=' ')
    print()