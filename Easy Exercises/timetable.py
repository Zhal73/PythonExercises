def timetable():
    line=""
    for i in range(0,100,10):
        for j in range (1,11):
            line = line + str(i+j) + "\t" 
        line = line + "\n"
    return line


print(timetable())


