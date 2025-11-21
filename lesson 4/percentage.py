print("enter the marks obtained by four subject")
maths = int(input("enter your maths mark :" )) 
english = int(input("enter your english mark :" )) 
hindi = int(input("enter your hindi mark :" )) 
science = int(input("enter your science mark :" )) 

sum = maths+english+hindi+science
percentage = (sum/400)*100
print("the percentage obtained :" , percentage)
