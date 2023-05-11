stri = input()
sum = 0
for i in stri:
    if i == "a" or i == "A":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum(1 * 2)
        else:
            sum = sum + 1
    elif i == "b" or i == "B":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (2 * 2)
        else:
            sum = sum + 2
    elif i == "c" or i == "C":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (3 * 2)
        else:
            sum = sum + 3
    elif i == "d" or i == "D":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (4 * 2)
        else:
            sum = sum + 4
    elif i == "e" or i == "E":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (5 * 2)
        else:
            sum = sum + 5
    elif i == "f" or i == "F":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (6 * 2)
        else:
            sum = sum + 6
    elif i == "g" or i == "G":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (7 * 2)
        else:
            sum = sum + 7
    elif i == "h" or i == "H":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (8 * 2)
        else:
            sum = sum + 8
    elif i == "i" or i == "I":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (9 * 2)
        else:
            sum = sum + 9
    elif i == "j" or i == "J":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (10 * 2)
        else:
            sum = sum + 10
    elif i == "k" or i == "K":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (11 * 2)
        else:
            sum = sum + 11
    elif i == "l" or i == "L":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (12 * 2)
        else:
            sum = sum + 12
    elif i == "m" or i == "M":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (13 * 2)
        else:
            sum = sum + 13
    elif i == "n" or i == "N":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (14 * 2)
        else:
            sum = sum + 14
    elif i == "o" or i == "O":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (15 * 2)
        else:
            sum = sum + 15
    elif i == "p" or i == "P":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (16 * 2)
        else:
            sum = sum + 16
    elif i == "q" or i == "Q":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (17 * 2)
        else:
            sum = sum + 17
    elif i == "r" or i == "R":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (18 * 2)
        else:
            sum = sum + 18
    elif i == "s" or i == "S":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (19 * 2)
        else:
            sum = sum + 19
    elif i == "t" or i == "T":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (20 * 2)
        else:
            sum = sum + 20
    elif i == "u" or i == "U":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (21 * 2)
        else:
            sum = sum + 21
    elif i == "v" or i == "V":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (22 * 2)
        else:
            sum = sum + 22
    elif i == "w" or i == "W":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (23 * 2)
        else:
            sum = sum + 23
    elif i == "x" or i == "X":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (24 * 2)
        else:
            sum = sum + 24
    elif i == "y" or i == "Y":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (25 * 2)
        else:
            sum = sum + 25
    elif i == "z" or i == "Z":
        if ord(i) < 96 and ord(i) != 32:
            sum = sum + (26 * 2)
        else:
            sum = sum + 26
len_sum = len(str(sum))
if len_sum < 6:
    x = 6 - len_sum
    sum = sum * (10**x)
print(sum)
