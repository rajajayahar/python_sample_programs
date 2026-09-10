"""customer_name=input("custer name: ")
product_name=input("product name")
quantity=input("quantity")
price_per_amount=input("price oer amount")
membership_type=input("membership_type").split(",")
print("customer_name: ", customer_name)
print("product_nmae:" , product_name)
print("quantity:" , quantity)
print("price per amount:" ,price_per_amount)
print("membership type:" ,membership_type)"""
"""
price_per_product=int(100)
quantity=int(9)
total_product_cost=int(price_per_product*quantity)
gst_added=int(quantity*10)
discount=int(20*quantity)
final_bill_amount=int(total_product_cost+gst_added-discount)
available_wallet_balance =int(1000-final_bill_amount)

print("price per amount:",price_per_product)
print("total quantity:",quantity)
print("total product cost:",total_product_cost)
print("gst added:",gst_added)
print("discont:",discount)
print("final amount:",final_bill_amount)
print("wallet balance:",available_wallet_balance)

price_per_product=int(100)
delivery_charge=int(50)
delivery_charge += (price_per_product)
discount=20
discount = delivery_charge - discount


print("price per product:" ,price_per_product)
print("delivery charge:" ,delivery_charge)
print("discount:" ,discount)
"""
"""
wallet_balance=int(input("check balance"))
if wallet_balance<=1000:
   print("balance available")
else:
    print("ensuffient balance")   """
"""
bill_amount=int(input("enter bill amount")) 
entered_membership=input("select member ship")
membership="gold"
if bill_amount > 1000 and membership==entered_membership:
    print("you have the free delivery")
else:
    print("you missed the free delivery")     """
"""
customer_press=int(input("enter days"))
bill_calculation=int(input("enter total bill"))
if customer_press > 200 or bill_calculation > 1500:
    print("customer is regular")
else:        
    print("not a regular customer")"""
"""
a=8
b=4
c=2
d=6
e=9
f=2
g=5



print(a & b)
print(c | d)
print(e ^ f)
print(g << 1)
print(g >> 1) """
"""

products=["rice","sugar","oil","milk","bread"]
products_name=input("enter product")
if products_name in products:
    print("avilable")
else:
    print("not available")  
"""      
"""
products=["rice","sugar","oil","milk","bread"]
products_name=input("enter product")
if products_name not in products:
    print("want to buy")
else:
    print("already buy")    
"""        
"""
product1=["rice","wheat","snacks","fish"]
product2=["rice","wheat","snacks","fish"]
print(product1 is product2)
print(product1 == product2)
"""
"""
product1=["rice","wheat","snacks","fish"]
product2=["rice","wheat","snacks","fish"]
print(product1 is not product2)
print(product1 is product2)
"""
#mini calculator
"""
a=int(input("a"))
b=int(input("b"))
operater=input( "add | sub | div | mul | per" )
if operater=="add":
    print(a+b)
elif operater=="sub":
    print(a-b)
elif operater=="div":
    print(a/b)
elif operater=="mul":
    print(a*b)
elif operater=="per":
    print(a % b)    
else:
    print("invalid operator")     

""" 
"""
#various input in if 
score=int(input("enter score"))
if score>=70:
    name=input("name")
    age=input("age")
    location=input("location")
    print("eligible")
else:
    print("not eligible")   
"""
"""
salary=int(input("enter salary"))
age=int(input("enter age")) 
if(salary>=20000 or age<=25):
    print("loan has been aproved")
    required_loan=int(input("enter need loan"))
    if required_loan<=50000:
        print("you are eligible")
    else:
        print("maximum loan amount is 50000")        
else:
    print("your loan is not eligible")
"""
"""
a=int(input("tamil:"))
b=int(input("english:"))
c=int(input("physics:"))
d=int(input("botany:"))
e=int(input("chemistry:"))
f=int(a + b + c + d + e )
print("total amrk: ",f)
if f/5<35:
    print("additional class is required")
else:
    print("you good to go")    
"""    
"""
#for loop
for i in ("apple"):
   print(i)
"""   
"""
for i in range (1,11):
    print(i,"x5=",i*5)     

for i in range (1,11,2):     
    print(i,"x2=",i*2)     
"""
"""
#map

numbers = [1,2,3,4,5,]
result = map(lambda a:a*3 ,numbers)
print(list(result)) 

names = ["RAJA", "KUMAR", "JAYAHAR"]
convert = map(lambda name: name.lower() ,names)
print(list(convert))

price = [100,200,300,400]
result = map(lambda a:a+(a*0.18),price)
print(list(result)) 


#sorted

numbers = [3,4,8,6,1,9,2]
result = sorted(numbers)
print(list(result))

names = ["Raja", "Arun", "Kumar", "Bala", "Vijay"]
arrange=sorted(names)
print(list(arrange))

#desending order

numbers = [3,4,8,6,1,9,2]
result = sorted(numbers,reverse=True)
print(list(result))

#filter
number=[20,40,35,67,68,50]
result=filter(lambda a: a%2==0,number)
print(list(result))

ages = [12, 18, 25, 15, 30, 10, 21]
peoples=filter(lambda age: age >= 18 ,ages)
print(list(peoples))

#filter() and map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=filter(lambda a:a%2==0,numbers)
calculate=map(lambda a:a*10,even)

print(list(calculate))

#filter() and sorted
numbers = [45, 12, 89, 3, 27, 60, 10, 75]
greater=filter(lambda a:a>30,numbers)
fix=sorted(greater,reverse=True)
print(list(fix))

salaries = [25000, 45000, 18000, 60000, 35000, 15000]
greater=filter(lambda a:a>30000,salaries)
fix=sorted(greater,reverse=True)
print(list(fix))
"""
#datastructures
#.slicing,string method ,list
title="python programing"
print(title[2:8])

title="hello world"
print(title[::-1])

name="python programming"
print(name.upper())

name="python programming"
print(name.lower())

name="python programming"
print(name.title())

fruits=["apple","banana","orange","water melon"]
fruits[0]="straberry"
print(fruits)
fruits.remove("orange")
print(fruits)