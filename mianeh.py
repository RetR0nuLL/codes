a = int(input("a?"))
b = int(input("b?"))
c = int(input("c?"))
d = int(input("d?"))
e = int(input("e?"))

#checking for even numbers!
if (a != b and a != c and a != d and a != e and b!=c and b != d and b != e and c != d and c != e and d != e):
    mylist = [a,b,c,d,e]

    #sorting

    if mylist[0] < mylist[1]:   
        temp = mylist[0]
        mylist[0] = mylist[1]
        mylist[1] = temp
    if mylist[0] < mylist[2]:
        temp = mylist[0]
        mylist[0] = mylist[2]
        mylist[2] = temp
    if mylist[0] < mylist[3]:
        temp = mylist[0]
        mylist[0] = mylist[3]
        mylist[3] = temp
    if mylist[0] < mylist[4]:
        temp = mylist[0]
        mylist[0] = mylist[4]
        mylist[4] = temp
    if mylist[1] <mylist[2]:
        temp = mylist[1]
        mylist[1] = mylist[2]
        mylist[2] = temp
    if mylist[1] < mylist[3]:
        temp = mylist[1]
        mylist[1] = mylist[3]
        mylist[3] = temp
    if mylist[1] < mylist[4]:
        temp = mylist[1]
        mylist[1] = mylist[4]
        mylist[4] = temp
    if mylist[2] <mylist[3]:
        temp = mylist[2]
        mylist[2] = mylist[3]
        mylist[3] = temp
    if mylist[2] < mylist[4]:
        temp = mylist[2]
        mylist[2] = mylist[4]
        mylist[4] = temp
    if mylist[3] < mylist[4]:
        temp = mylist[3]
        mylist[3] = mylist[4]
        mylist[4] = temp

    #printing the middle num!

    print(f"\n\n(({mylist[2]}))")
else:
    print("there are even numbers, restart the program and avoid entering even numbers!")

#bubble sort
"""
lis=[a,b,c,d,e]
for i in range(4,0,-1):
    for k in range(0,i):
        if lis[k] < lis[k + 1]:
            temp = lis[k]
            lis[k] = lis[k+1]
            lis[k + 1] = temp
"""
#sorting by bulit-in function
"""
if (a != b and a != c and a != d and a != e and b!=c and b != d and b != e and c != d and c != e and d != e):
    mylist = [a,b,c,d,e]
    mylist = sorted(mylist)
    print(mylist[2])
else:
    print("there are even numbers, restart the program and avoid entering even numbers!")
"""