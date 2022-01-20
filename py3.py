details=[]
name=input("Enter your name")
age=int(input("Enter your age"))
occ=input("Enter your occupation")
add=input("Enter your address")
sal=int(input("Enter your salary"))
details.extend([name,age,occ,add,sal])
for i in details:
    print(i) 