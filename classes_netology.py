class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'      

    def _calculates_average_grade(self):
        average_grade = 0

        for grade in self.grades.values():
            average_grade+= sum(grade) / len(grade)

        return round(average_grade / len(self.grades), 1)
        
    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}\n'
        average_grade = f'Средняя оценка за домашние задания: {self._calculates_average_grade()}\n'
        courses_in_progress = f'Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\n'
        finished_courses = f'Завершенные курсы: {" ".join(self.finished_courses)}\n'

        return name + surname + average_grade + courses_in_progress + finished_courses

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._calculates_average_grade() < other._calculates_average_grade()    

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _calculates_average_grade(self):
        average_grade = 0

        for grade in self.grades.values():
            average_grade+= sum(grade) / len(grade)

        return round(average_grade / len(self.grades), 1)

    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}\n'
        average_grade = f'Средняя оценка за лекции: {self._calculates_average_grade()}\n'

        return name + surname + average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._calculates_average_grade() < other._calculates_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}\n'
        surname = f'Фамилия: {self.surname}\n'        

        return name + surname
 
def calculates_average_grade_for_homework_for_all_students_within_overall_course(students, course):
    average_grade = 0
    count = 0

    for student in students:
        if course in student.grades:
            average_grade+= sum(student.grades[course]) / len(student.grades[course])
            count+= 1

    return round(average_grade / count, 1)

def calculates_average_grade_for_all_lecturer_within_overall_course(lecturers, course):
    average_grade = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.grades:
            average_grade+= sum(lecturer.grades[course]) / len(lecturer.grades[course])
            count+= 1

    return round(average_grade / count, 1)



student_mikhail = Student('Mikhail', 'Latishev', 'male')
student_mikhail.courses_in_progress += ['Python', 'Java']

student_pavel = Student('Pavel', 'Pupkin', 'male')
student_pavel.courses_in_progress += ['Java']
student_pavel.finished_courses += ['Python']
 
lecturer_alexey = Lecturer('Alexey', 'Bulygin')
lecturer_alexey.courses_attached += ['Python']

lecturer_andrey = Lecturer('Andrey', 'Makarov')
lecturer_andrey.courses_attached += ['Java']

reviewer_alexander = Reviewer('Alexander', 'Bardin')
reviewer_alexander.courses_attached += ['Python', 'Java']

reviewer_danil = Reviewer('Danil', 'Danilov')
reviewer_danil.courses_attached += ['Java']

reviewer_alexander.rate_hw(student_mikhail, 'Python', 8)
reviewer_alexander.rate_hw(student_mikhail, 'Python', 10)
reviewer_alexander.rate_hw(student_mikhail, 'Python', 9)

reviewer_alexander.rate_hw(student_mikhail, 'Java', 5)
reviewer_danil.rate_hw(student_mikhail, 'Java', 8)
reviewer_alexander.rate_hw(student_mikhail, 'Java', 4)

reviewer_alexander.rate_hw(student_pavel, 'Java', 4)
reviewer_danil.rate_hw(student_pavel, 'Java', 3)
reviewer_danil.rate_hw(student_pavel, 'Java', 1)

student_mikhail.rate_lecturer(lecturer_alexey, 'Python', 10)
student_mikhail.rate_lecturer(lecturer_alexey, 'Python', 9)
student_mikhail.rate_lecturer(lecturer_alexey, 'Python', 10)
student_mikhail.rate_lecturer(lecturer_andrey, 'Java', 6)

student_pavel.rate_lecturer(lecturer_andrey, 'Java', 10)
student_pavel.rate_lecturer(lecturer_andrey, 'Java', 9)
student_pavel.rate_lecturer(lecturer_andrey, 'Java', 6)


print(f'Оценки студента {student_mikhail.name} {student_mikhail.surname}: {student_mikhail.grades}\n')
print(f'Оценки студента {student_pavel.name} {student_pavel.surname}: {student_pavel.grades}\n')

print(f'Оценки лектора {lecturer_alexey.name} {lecturer_alexey.surname}: {lecturer_alexey.grades}\n')
print(f'Оценки лектора {lecturer_andrey.name} {lecturer_andrey.surname}: {lecturer_andrey.grades}\n')

print(student_mikhail)
print(student_pavel)

print(lecturer_alexey)
print(lecturer_andrey)

print(reviewer_danil)
print(reviewer_alexander)

if lecturer_alexey < lecturer_andrey:
    print (f'Оценки лектора {lecturer_andrey.name} лучше оценок лектора {lecturer_alexey.name}')
else:
    print (f'Оценки лектора {lecturer_alexey.name} лучше оценок лектора {lecturer_andrey.name}')

if student_mikhail < student_pavel:
    print (f'Оценки студента {student_pavel.name} лучше оценок студента {student_mikhail.name}')
else:
    print (f'Оценки студента {student_mikhail.name} лучше оценок студента {student_pavel.name}')

java_students_average_grade = calculates_average_grade_for_homework_for_all_students_within_overall_course([student_mikhail, student_pavel], 'Java')
print(f'\nСредняя оценка за дз по всем студентам в рамках курса Java = {java_students_average_grade}')

java_lecturers_average_grade = calculates_average_grade_for_all_lecturer_within_overall_course([lecturer_alexey, lecturer_andrey], 'Java')
print(f'\nСредняя оценка лекторов в рамках курса Java = {java_lecturers_average_grade}')