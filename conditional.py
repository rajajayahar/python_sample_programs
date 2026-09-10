"""
if condition;
code to executed
elif;
 condition
go to executed 
else;
code to be executed
"""
"""number=int(input("enter a numper"))
if number >=0:
    print("positive number")
else:
    print ("negative number")"""

"""vowelchecker =input("enter a character")    
if vowelchecker in "aeiouAEIOU":
    print("entered char is a vowel")
else:
    print("enter char is a consonant")

num=int(input("enter a numper"))
if num%2==0:
   print("num is even")
else:
    print("num is odd")"""

"""age=int(input("enter a age"))
if age<=13:
   print("child")
elif age<18:
   print("teenager")
elif age<60:
   print("adult")
else:
    print("senior citizen")"""
"""
num=int(input("enter a numper"))
if num>=0:
    if num%2==0:
        print("number is positive and even")
    else:
        print("number is possitive and odd")
else:
    print("negative number")"""

#check wether the given num is 3 digit or not
"""num=int(input("enter the number"))
if(num>99<1000):
   print("the enter num is 3 digit")
else:
    print("num is not 3 digit")"""

'''score=int(input("enter mark"))
if(score<35):
   print("poor student")
elif(score>35 and score<70):   
   print("average student")
elif(score>71):
   print("good") 

else:   
    print("fail")'''

 #for and while are entry controlled loops
 

"""for variable in sequence:
    code to be executed

  #using range function 
  for variable in range(start,stop,step:):
    code to be executed

start=dfault value is 0       
start =default value is 0
stop=number-1
step=default value is 1 for possitive number and for negative
numbers we need to assigun

#syntax for while loop:
initialization
while condition:
    code to be executed
    updation"""
"""

word=input("enter a word:")
for letter in word:
    print(letter)
"""
"""
for element in range(11):
    print(element)
for element in range(5,15):
    print(element)    
"""

"""for element in range(10,26,5):
    print (element)"""

"""for item in range(10,1,-2): #- value is used for only in desindig order
    print(item)  
"""
"""
for item in range(17,3,-3):
    print(item) """

"""multiplay=int(input("ente anumber: "))
for item in range(6,18):
      print(item*multiplay) """
"""
multiplay=int(input("ente anumber: "))
for item in range(6,18):
      #print(multiplay,"*",item,"=",item*multiplay)      
       print(f"{multiplay}*{item}={item*multiplay}")
"""       
"""
value=5
iterations=int(input("enther the number of iterations: "))
while value <=iterations:
    print(value)
    value+=2 """
"""
value=("hello")
iterations=(input("enther the number of iterations: "))
while value:
    print(value)
"""
"""
#jumping statementes
for i in range(1,11):
    if i == 4:
       pass
    print(i)

for i in range(1,10):
    if i == 5:
        continue
    print(i)    
 print("1.check balance") 
    
for i in range(2,8):
    if i == 6:
        break
    print(i)    


        
    for i in range (1,20):
        if i == 5:
            continue
        if i == 12:
            pass
        if i == 17:
            break
        print(i)                      

"""    

correct_pin=(1234)
for i in range(3):
   pin=int(input("enter pin"))
   if correct_pin == pin:
    print("login succesfully")
    while True:
        print("1.balance")
        print("2.deposit")
        print("3.withdraw") 
        print("4.exit")
    
        choice=int(input("enter choice"))
        if choice < 1 or choice > 4:
           print("invalid option")
           continue
        elif choice == 1:
            pass
            print("balance")
        elif choice == 2:
            print("deposit")
        elif choice == 3:
            print("withdraw")
        elif choice == 4:
            print("thank you")
            break
        
    break
else:
    print("invalid pin")
     
    
    
       