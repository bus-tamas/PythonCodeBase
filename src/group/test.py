import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def process_marks(records):
    students = []
    for record in records:
        name, email, *marks = record.split(',')
        if len(marks) != 3 or not all(mark.isdigit() and int(mark) >= 35 for mark in marks):
            continue
        if not validate_email(email):
            continue
        marks = list(map(int, marks))
        total_marks = sum(marks)
        students.append((name, email, marks, total_marks))

    students.sort(key=lambda x: x[3], reverse=True)
    rank = 0
    prev_total_marks = None
    for i, student in enumerate(students):
        if student[3] != prev_total_marks:
            rank = rank + 1
            prev_total_marks = student[3]
        students[i] = student + (rank,)

    return students

# Test the program with the given sample input
sample_input = [
    "11",
    "Name-0,name0@gmail.com,80,92,80",
    "Name-1,name1@gmail.com,87,94,95",
    "Name-2,name2@gmail.com,98,95,78",
    "Name-3,name3@gmail..com,92,63,76",
    "Name-4,name4@gmail.com,90,86,88",
    "Name-5,name5@gmail.com,98,85,80",
    "Name-6,name6@gmail.com,83,,84",
    "Name-7,name7@gmail.com.,80,76,86",
    "Name-8,name 8@gmail.com,92,83,76",
    "Name-9,name9@gmail.com,90,95,86",
    "Name-10,name10@gmail.com,82,0,80"
]

num_records = int(sample_input[0])
records = sample_input[1:]

result = process_marks(records)

# Print the output
for i in range(len(result)):
    name, email, marks, total_marks, rank = result[i]
    marks_str = ','.join(str(mark) for mark in marks)
    print(f"{name},{email},{marks_str},{total_marks},{rank}")
