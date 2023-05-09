a = int(input("first num!?"))
b = int(input("second num!?"))
c = int(input("third num!?"))
max = 0 
min = 0
vast = 0
if (((not a == b)) and (not (b == c))  and  (not (a == c))):
    

    if( a < b and a < c):  min = a
    elif( b < a and b < c):  min = b
    elif( c < b and c < a):  min = c
    if ( a > b and a > c):  max = a
    elif ( b > a and b > c):  max = b
    elif ( c > b and c > a):  max = c
    if((a == max and b == min) or (a==min and b ==max)):     vast = c
    elif((a == max and c == min) or (a==min and c ==max)):     vast = b
    else:     vast = a
    my_list = [max , vast , min]
    print(my_list)
else:
    print("there are equal numbers!")

# 5 adad a b c d e darim ke az karbar migirim , agar adad tekrari vojood dasht ba yek peqam khata barname tamam shavad , da qeyr in soorat adad Mianeh ra peyda konid!!