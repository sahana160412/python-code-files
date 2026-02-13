student_data={'id1':
              {
                  'name':['zara'],
                  'class':['v'],
                  'subject':['maths','science','social']
              },

              'id2':{
                  'name':['jack'],
                  'class':['v'],
                  'subject':['maths','english','social']
                  
              },

              'id3':{
                  
                  'name':['zara'],
                  'class':['v'],
                  'subject':['maths','science','social']
              },

              'id4':{
                  'name':['idila'],
                  'class':['v'],
                  'subject':['maths']
              }

 }

result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value

print(result)