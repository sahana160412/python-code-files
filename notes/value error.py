try:
    tr=int(input('Enter the number:'))
    print('entered number',tr)
except ValueError as e:
    print('ValueError:',e)



