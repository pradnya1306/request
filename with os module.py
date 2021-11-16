import requests
import json
import os
file=os.path.exists("courses.json")
if file ==True:
    with open("courses.json","r")as m:
        data=json.load(m)
    print("courses name :-")
    for i in range (len(data)):
        for j,p in data[i].items():
            if j=="name":
                print(i+1,p,data[i]["id"])

    choose=int(input("which course do you want choose :  "))
    choose1=choose-1
    print(data[choose1]["name"])
    print(data[choose1]["id"])

else :
    print("this file is not exists")
    

file=os.path.exists("courses_exercise.json")
if file ==True:
    with open("courses_exercise.json","r")as n:
        edata=json.load(n)
    
    serial_number2=1
    serial_number3=1
    # new_no=1
    list1=[]
    list2=[]
    for j in edata["course"]["exercises"]:
        
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            print("  ",serial_number3," ",j["slug"])
            serial_number2+=1
            
            # new_no=1
            list1.append(j)
            list2.append(j)
            
        elif j["parent_exercise_id"]==j["id"]:
            print(serial_number2,j["name"])
            serial_number2+=1
            list1.append(j)
            new_no=1
            
        elif  j["parent_exercise_id"]!=j["id"]:
        
            print(" ",new_no,j["name"])
            new_no+=1
            list2.append(j)
    with open(" list1.json","w")as f:
        json.dump(list1,f,indent=4)  
    with open("list2.json","w")as f:
        json.dump(list2,f,indent=4)

else:
    print ("this file is not exists")
    

file=os.path.exists("/home/pradnya/Desktop/request/ list1.json")
if file ==True:
    with open("/home/pradnya/Desktop/request/ list1.json","r")as a:
        fdata=json.load(a)
    parent=int(input("enter the parent exercise do want:"))
    for k in list1:
        if k["parent_exercise_id"]==k["id"]:
            print(list1[parent-1]["name"])
            # num=(list1[parent-1]["id"])
            break
    var=[]
    var3=[]
    num=(list1[parent-1]["id"])
    new_no1=1
    for n in list2:
        if n["parent_exercise_id"]==num:
            print(" ",new_no1,n["name"])
            var.append(n["name"])
            var3.append(n["content"])
            new_no1+=1
else:
    print ("this file is not exists")


file=os.path.exists("/home/pradnya/Desktop/request/list2.json")
if file ==True:
    with open("/home/pradnya/Desktop/request/list2.json","r")as b:
        evar=json.load(b)
    child=int(input("enter the child exercise do u want :"))
    # new_no2=1
    for s in range(len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])
    
            
else:
    print("this file is not exists")
    

        
        
        








                