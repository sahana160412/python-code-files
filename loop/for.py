n=int(input("enter the number whose sum you want to find out:"))
sum=0
for n in range(1,n+1):
    print("sum of ",n," and ",sum," is ")
    sum=sum+n 
    print(sum)