isbn = input("insert the first 12 digit of the ISB number: ")
total = 0
for i in range(len(isbn)):
    if (i+1)%2!=0:
        total=total+int(isbn[i])
    else:
        total=total+3*int(isbn[i])
total = 10- total % 10

print("the checksum is: ", total)

978030640615