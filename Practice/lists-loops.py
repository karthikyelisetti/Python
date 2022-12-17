studentMarks = [12, 30, 45, 60, 70]
studentNames = ["name1", "name2", "name3", "name4", "name5"]
lengthList = len(studentMarks)
for i in range(0, lengthList):
    if (studentMarks[i] > 30):
        print(studentNames[i])
