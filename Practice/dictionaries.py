students = [{
    "name": "Sanjoy",
    "marks": 12,
},
    {
    "name": "Sanpreet",
    "marks": 40
},
    {
    "name": "Adithya",
    "marks": 50
}]

for i in range(0, len(students)):
    if (students[i]["marks"] > 30):
        print (students[i]["name"])