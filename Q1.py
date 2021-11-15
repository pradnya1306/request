import requests
import json
x=requests.get('https://api.merakilearn.org/courses')
# data=json.loads(x.text)
data=x.json()
with open("courses.json","w") as y:
    json.dump(data,y,indent=4)


print("courses name :-")
for i in range (len(data)):
   for j,p in data[i].items():
       if j=="name":
           print(i+1,p,data[i]["id"])

choose=int(input("which course do you want choose :  "))
choose1=choose-1
print(data[choose1]["name"])
print(data[choose1]["id"])

h=requests.get("https://api.merakilearn.org/courses/"+data[choose1]["id"]+" "+ "/exercises")
# edata=json.loads(h.text)
edata=h.json()
with open("courses_exercise.json","w")as n:
    json.dump(edata,n,indent=4)

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
                       
u1=input("what do u want previous or next(n/p):")
if u1=="p":
    print("courses name :-")
    for i in range (len(data)):
        for j,p in data[i].items():
            if j=="name":
                print(i+1,p,data[i]["id"])
    choose=int(input("which course do you want choose :  "))
    choose1=choose-1
    print(data[choose1]["name"])
    print(data[choose1]["id"])

    h=requests.get("https://api.merakilearn.org/courses/"+data[choose1]["id"]+" "+ "/exercises")
    # edata=json.loads(h.text)
    edata=h.json()
    with open("courses_exercise.json","w")as n:
        json.dump(edata,n,indent=4)

    serial_number2=1
    serial_number3=1
    list1=[]
    list2=[]
    for j in edata["course"]["exercises"]:
        # serial_number3=1
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            print(" ",serial_number3,j["slug"])
            serial_number2+=1
            new_no=1
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


u2=input("what do u want previous or next(n/p):")
if u2=="p":
    serial_number2=1
    serial_number3=1
    list1=[]
    list2=[]
    for j in edata["course"]["exercises"]:
        # serial_number3=1
        if j["parent_exercise_id"]==None:
            print(serial_number2,j["name"])
            print(" ",serial_number3,j["slug"])
            serial_number2+=1
            new_no=1
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

    child=int(input("enter the child exercise do u want :"))
    # new_no2=1
    for s in range(len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])
    u4=input("what do u want previous or next(n/p):")
    if u4=="p":
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
        child=int(input("enter the child exercise do u want :"))

        for s in range(len(var)):
            if (child-1)==s:
                print(var[s])
                print(var3[s])

else:
    child=int(input("enter the child exercise do u want :"))
    # new_no2=1
    for s in range(len(var)):
        if (child-1)==s:
            print(var[s])
            print(var3[s])
    u3=input("what do u want previous or next(n/p):")
    if u3=="p":
        child=int(input("enter the child exercise do u want :"))

        for s in range(len(var)):
            if (child-1)==s:
                print(var[s])
                print(var3[s])

            # new_no2+=1
    # elif u1=="n":
# with open("topic1.json","w")as f:
#         json.dump(var,f,indent=4)
# with open("topic1.json","w")as t:
#         json.dump(var3,t,indent=4)
        

	
	
	








            