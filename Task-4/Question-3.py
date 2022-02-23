a1=['Roll no','Name','Marks']
l=[a1]
n=int(input("Enter the number of records you wanted to add:"))
# i)
for i in range(n):
    print()
    print('Record number',i+1)
    print()
    b1=input("Enter your Rollno:")
    b2=input("Enter your name:")
    b3=input("Enter your Marks:")
    a2=[b1,b2,b3]
    l.append(a2)
for i in l:
    if i[0]=='Roll no':
        print(i[0]+'   '+i[1]+'   '+i[2])
    else:
        print(3*' '+i[0]+3*'  '+i[1]+3*'  '+i[2])

# ii)
if len(l)<3:
    print("The no of record is less than 2")
else:
    print("Second record/row")
    print(l[2][0]+'  '+l[2][1]+'  '+l[2][2])
    