def near(first,second):
    if len(first)==len(second) or len(first) < len(second) or abs(len(first)-len(second)) > 1:
        return False
    else:
        for i in range(len(second)):
            if first[i] != second[i]:
                position = i
 #   temp = fist[:position] + first[position + 1:]
    if first[:position] + first[position + 1:] == second:        
        return True
    else:
        return False

print(near ("reset","rest"))
print(near ("dragoon","dragon"))
print(near ("eave","leave"))
print(near ("sleet","lets"))