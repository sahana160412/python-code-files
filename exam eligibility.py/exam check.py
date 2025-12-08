"""Write a program to check whether the student can take an exam or not. 
Students will be allowed only in two conditions: If they have a medical cause 
(‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. 
If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
"""
medical_cause=input("did you have a medical cause y or n:")
atten=int(input("enter the attendance of the student:"))

if medical_cause== 'y':
   print("you are allowed")
else :
    if atten >=75:
        print("you are allowed ")
    else:
        print("not allowed")
