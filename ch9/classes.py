# 클래스(Classes) - 설계도

class Student:
    def __init__(self, name, major) -> None:
        self.name = name
        self.major = major
        self.is_graduated = False
        
    def study(self) -> None:
        print(f"{self.name} 학생은 공부 중입니다.")
    
    def edit_major(self, new_major):
        student_1.major = new_major
        print(f"{student_1.major}로 전공이 변경되었습니다.")


# 인스턴스 - 실체화된 사물

student_1 = Student('김멋사', '컴퓨터공학과')
print(student_1)


student_1_name = student_1.name
print(student_1_name)

student_1.study()


class ForeignStudent(Student):

    def __init__(self, name, major, country) -> None:
        super().__init__(name, major)
        self.country = country
    
    def study(self) -> None:
        print(f"{self.name} is studying now")

foreign_stud_1 = ForeignStudent("이테킷", "국어국문학과", "한국")
print(foreign_stud_1.name)
print(foreign_stud_1.major)
print(foreign_stud_1.is_graduated)

print("\n\n")

foreign_stud_1.study()
