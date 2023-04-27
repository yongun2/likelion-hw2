# 딕셔너리(Dictionaries)

student = {
    "student_no": "2023",
    "major": "English",
    "grade": 1
}


student["student_no"] = "2023232"


# 추가
student["gpa"] = 4.5
print(student)

# 수정
student["gpa"] = 4.3
print(student)

# 삭제
del student["grade"]
print(student)

print("\n\n")

# 데이터 접근
print(student.get("gpads", "해당 키-값 쌍이 없습니다."))

# 딕셔너리의 키를 반환
print(student.keys())
print(list(student.keys()))


# 딕셔너리 값을 반환
print(list(student.values()))
print("\n\n")

tech = {
    "HTML": "Advanced",
    "JavaScript": "Intermediate",
    "Python": "Expeort",
    "Go": "Novice"
}

for i in tech:
    print(i)


for key, value in tech.items():
    print(f"{key} - {value}")

print('\n\n')

# 중첩(Nesting)

student_1 = {
    "student_no": "1",
    "gpa": "4.3",
}

student_2 = {
    "student_no": "2",
    "gpa": "3.8",
}

students = [student_1, student_2]

for student in students:
    student["graduated"] = False
    print(student)



student = {
    "subjects": ["회계원리", "중국어회화"]
}

print(student["subjects"])

subjects_list = student["subjects"]
for subject in subjects_list:
    print(subject)


student = {
    "scholarship": {
        "name": "국가장학급",
        "amount": "1000000"
    }
}

print(student)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)