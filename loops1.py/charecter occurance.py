string=input('please enter  your full word:')
char=input('please enter your own charecter:')
i=0
count=0
while(i<len(string)):
    if string[i]==char:
        count=count+1
    i=i+1
print('The total Number of times ',char,' is appearing is ',count)