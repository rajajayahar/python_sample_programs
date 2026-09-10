#data structure
#.immutable data
#.string > immutable
#.list represent[] order collection,mutable,alow dublicates,can be asses using indexing
#.tuple ()order collection,immutable,alow dublicates,can be asses using indexing
#.set {}unordered collection, mutable,does'nt allow duplicates,cannot be acces using indexing
#dictionary {key:value}ordered collection,key cannt be changed ,value can be changed,allow duplicate values,can be using indexing 
"""
username="raja"
"""
"""
 0   1  2  3 #indexing indxing return a single value
-4  -3 -2 -1
 r   a  j  a
 1   2  3  4  #

"""
"""
print(username[2])
print(len(username))

print(username[-2])
print(len(username))
"""
"""
#slicing slicing returns set of values
#[start:stop:step]
#start-start default value is 0
#stop-value -1
#step-numer of skips(defaultly 1 for positive numbers)
data="python is a programming language"
print(data[:8])
print(data[2:8])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2]) #it will not work
print(data[10:1:-2])
print(data[::-1])
print(data[::-2])
"""
"""
#string methods
text="hellow i am raja" 
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.startswith("yt"))
print(text.startswith("he"))
print(text.endswith("ja"))
"""
"""text[0]="r"
print(text)
"""
"""
print(id(text))
uppercase=text.upper()
print(id(uppercase))
"""
#list
#crud operation
#list creation
#list view
#list updating
#list deleting
"""
userdata=["raja",21,"tvm"]
print(userdata)
userdata.insert(1,"maria")
userdata.append(2026)
userdata.extend("python")
userdata.append(["english","hindi","tamil"])

print(userdata)
print(userdata[11])
print(userdata[11][0])
userdata.extend(["raja","yajahar"])
print(userdata)
userdata[0]="RAJA"
print(userdata)

userdata.remove("tvm")
print(userdata)
userdata.pop(3)
print(userdata)
userdata.reverse()
print(userdata)
"""
"""
#tuple-()-immutable data structure
tuple1=(1,2,3,4,5)
print(tuple1)
#nested tuple
tuple2=("raja","jayahar","chandru",(1,2,3))
print(tuple2[3])
print(tuple2[0])
print(tuple2[1])
print(tuple2[2])
print(tuple2[3][0])
print(tuple2[3][1])
print(tuple2[3][2])



#tuple unpacking
person=("raja",22,"mtm")
name,age,place=person
print(name)

num=(10,20,30,40,50)
e,*f,g=num
print(f)

num1=(10,20,30,40,40,50)
a,b,*c,d=num1
print(*c)
print(num1.count(40))#how many numbers
print(num1.index(30))#which place in number
print(num1[2])#2 place having number

name=input("enter a name: ")
count=0
for  char in name:
    count+=1
print("the count is:",count)   
"""
"""
letter=input("enter a words: ")
for char in letter:
    if letter.count(char) == 1:
        
       print("frist non-repeating characters is: ",char)
       break
else:
        print("non repeating character")
"""   
"""     
#repeating charcter index,second on repeating character,without using the count function
letter=input("enter a words: ")
freq={}
for char in letter:
    if char in freq:
        freq[char] += 1
    else:
        freq[char]  = 1  
found = 0        
    
for char in letter:
    if freq[char] == 1:
        found += 1

        if found == 2:
        

      
           print(letter.index(char))
           break
"""
"""
#set-{}-unordered structures -mutable-no duplicates
student1={"english","tamil","hindi"}
student2={"english","hindi","python"}
student3={"python","java"}
student1.add("c")
#student1.add("kannada","marati")#only one argument just like append
print(student1)
student1.update(["c++","java",])#for more elements
print(student1)
student1.pop()
print(student1)
student1.remove("java")
print(student1)
student1.remove("arabi")# not working coming error becase there arabi not list
print(student1) 

#union,intersection,difference,symmrtric difference
"""
"""
student1={"raja","biju","arwin","chandhru"}
student2={"vinish","benhin","raja","chandhru"}
student3=student1.union(student2)
print(student3) #comenly having value  comes but repeatly comes value has been notexecuted

student1={"raja","biju","arwin","chandhru"}
student2={"vinish","benhin","raja","chandhru"}
student3=student1.intersection(student2)
print(student3)# same value only executed

student1={"raja","biju","arwin","chandhru"}
student2={"vinish","benhin","raja","chandhru"}
student3=student1.difference(student2)
print(student3)#having in a but not in b

#union > |
print(student1.union(student2))
print(student1 | student2)
#intersection > &
print(student1.intersection(student2))
print(student1 & student2)
#difference > -
print(student1.difference(student2))
print(student1 - student2)

#symmmetricdifference >  #commenly having elements will deleted and give other values
print(student1.symmetric_difference(student2))
"""
"""
#issubset,issuperset,disjoint
#issubset
a={1,2,3,4}
b={2,3,4,1,0,9}
print(a.issubset(b))#a set a is a subset of b if every element of a is also present b
#issuperset
a={1,2,3,4}
b={2,3,4,1,0,9}
print(b.issuperset(a))#if b contains all elements of a,then b is a superset of a
#disjoint
a={1,2,3,4}
b={5,6,7,8,0,9}
print(b.isdisjoint(a))#two sets are disjoint when they have no common elements
"""
"""
#frozenset
fs1=frozenset("raja")
fs2=frozenset([1,2,3,4,2,3,4])
print(fs1)
print(fs2)
"""
"""
#dictionary
student={
    "name":"raja",
    "age":22,
    "place":"mtm"

}
print(student)
print(student["name"])

info=dict(city="tvm",state="tamil nadu")
print(info)
print(info.keys())
print(info.values())
#print(info["mark"])
student.pop("age")
print(student)

for key,value in student.items():
    if key=="name":
        print(key,value)
#nested
employe={
    "employe1":{
        "name":"raja",
        "age":22
    },
    "empolye2":{
        "name":"jayahar",
        "age" :21 
    },
    "empolye3":{
        "name":"biju",
        "age" :20
    } 

}
print(employe["empolye3"]["age"])
"""
student={
    "name":"raja",
    "age":22,
    "place":"mtm"

}
student["city"]="tck"
print(student)
student["place"]="tck"
print(student)
student.pop("age")
print(student)
print(student["name"])
print(student.keys())
print(student.values())
for keys,values in student.items():
    print(keys,values)

student={
    "student1":55,
    "student2":60,
    "studnet3":100

}
print(sum(student.values()))