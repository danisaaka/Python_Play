students = {
    "student1": {
        "name": "John",
        "age": 10,
        "grade": 5
    },
    "student2": {
        "name": "Alice",
        "age": 11,
        "grade": 6
    },
}

for student_key, student_info in students.items():
    print("Student Key: ", student_key)
    for info_key, info_value in student_info.items():
        print(info_key, ":", info_value)
