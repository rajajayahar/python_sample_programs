"""
store_data=open("new_file.txt","w")#file autometically created when given w
store_data.write("wellcome to python programs")
print(store_data)
store_data.close()


read_data=open("new_file.txt","r")
print(read_data.read())
read_data.close()

append_data=open("new_file.txt","a")
append_data.write("\npython is an interpreted language")
print(append_data) 
append_data.close()

read_data=open("new_file.txt","r")
print(read_data.read())
read_data.close()
"""
"""
#using context manager 

with open("new_file.txt","r") as f:
    print("current position: ",f.tell())#tell
    f.read(6)
    print("after read position is:",f.tell())
    f.seek(4)
    print("after seek :",f.tell())#seek
    print(f.read())

"""
"""
with open("nature.jpg","rb") as data:
    print(data.read())""" 
"""
data=open("delete_file.txt","x")#for open file
print(data)    
data.close()
"""
"""
file_path="delete_file.txt"#delete the file
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted succesfully")
else:
    print("file not exists")
"""

#serialization  
import pickle
data={
    "students":["raja","ajith","jayahar"]

} 

#serialization -saving data to file

with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
    print("data is serialized to user details")

#deserialization retrieving data
with open("user_details.pkl","rb") as f:
    pickle.load(f)
    print("data is deserialized from user details")   

#serialization saving data into memory

dump_data=pickle.dumps(data)
print("data is serialized to bytes: ",dump_data)

load_data=pickle.loads(dump_data)
print("deserialized data to bytes: ",load_data)  