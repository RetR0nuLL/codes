str = input("yek kalame vared koonid!\n")
upper = 0
lower = 0
for i in str:
    if (ord(i) >= 97 and ord(i) < 123):
        lower += 1
    elif (ord(i) <= 90 and ord(i) > 64):
        upper += 1
if upper == lower :
    print("\nTrue")
else:
    print("\nFalse")    