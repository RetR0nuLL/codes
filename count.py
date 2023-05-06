def finder(substring):
    global index
    global list_index
    global tedad
    for i in input_str :
        if index == andazeh:
            tedad += 1
            index = 0
            list_index = 0
        if substring[list_index] == i:
            index += 1
            list_index += 1
        else:
            index = 0
            list_index = 0
input_str = input("lotfan yek jomleh benevisid!\n")
substr = input("substr mored nazar ra vared konid!\n")
input_str += " "
andazeh = len(substr)
list_index = 0
index = 0
tedad = 0
finder(substr)
print(f"there are {tedad} {substr} in the string!!!!!")

