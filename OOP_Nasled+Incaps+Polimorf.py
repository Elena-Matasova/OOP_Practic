class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if grade not in range(1, 11):
            result = print('Выставленная студентом оценка не соответствует 10-балльной шкале')
            return result
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        total_sum = 0
        grades_count = 0
        for key, value in self.grades.items():
            total_sum += sum(value)
            grades_count += len(value)
        average = round((total_sum / grades_count), 1) if grades_count > 0 else 0
        return average

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)

        result = (f'Имя: {self.name}\n'
              f'Фамилия: {self.surname}\n'
              f'Средняя оценка за домашнее задание: {self._average_grade()}\n'
              f'Курсы в процессе изучения: {courses_in_progress_str}\n'
              f'Завершенные курсы: {finished_courses_str}\n')
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() == other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._average_grade() >= other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        total_sum = 0
        grades_count = 0
        for key, value in self.grades.items():
            total_sum += sum(value)
            grades_count += len(value)
        average = round((total_sum / grades_count), 1) if grades_count > 0 else 0
        return average

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self._average_grade()}\n')
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() == other._average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() > other._average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._average_grade() >= other._average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not 1 <= grade <= 10:
            return print('Оценка должна быть в диапазоне 1–10')
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')
        return result

def students_average_grade(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades.keys():
            total_sum = total_sum + sum(student.grades[course])
            total_count = total_count + len(student.grades[course])
    result = round(total_sum / total_count, 1) if total_count > 0 else 0
    return result

def lecturers_average_grade(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            total_sum = total_sum + sum(lecturer.grades[course])
            total_count = total_count + len(lecturer.grades[course])
    result = round(total_sum / total_count, 1) if total_count > 0 else 0
    return result

student1=Student("Лена", "Ленина", "Ж")
student1.finished_courses.append('Git')
student1.finished_courses.append('GitVerse')
student1.courses_in_progress.append('C++')
student1.courses_in_progress.append('Java')
student1.courses_in_progress.append('Python')
student1.grades['C++'] = [10, 9, 10, 9]
student1.grades['Java'] = [10, 10]
student1.grades['Python'] = [6, 8, 10]

student2=Student("Василий", "Васечкин", "M")
student2.finished_courses.append('C++')
student2.finished_courses.append('Java')
student2.courses_in_progress.append('Python')
student2.courses_in_progress.append('Git')
student2.grades['Git'] = [10, 9, 8]
student2.grades['Python'] = [8, 9]

print('Студент1:')
print(student1)
print('Студент2:')
print(student2)
print(f'Студент1, ср. оценка: {student1._average_grade()} < Студент2, ср. оценка: {student2._average_grade()} -> {student1 < student2}')
print(f'Студент1, ср. оценка: {student1._average_grade()} = Студент2, ср. оценка: {student2._average_grade()} -> {student1 == student2}')
print(f'Студент1, ср. оценка: {student1._average_grade()} > Студент2, ср. оценка: {student2._average_grade()} -> {student1 > student2}\n')

print(f"Средняя оценка всех студентов в рамках курса Python: {students_average_grade([student1, student2], 'Python')}\n")
print('-' * 50)

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Java')
student2.rate_lecture(lecturer1,'Python',5)
student1.rate_lecture(lecturer1,'Java',10)

lecturer2 = Lecturer('Сергей', 'Сергеев')
lecturer2.courses_attached.append('Git')
lecturer2.courses_attached.append('C++')
lecturer2.courses_attached.append('Python')
student1.rate_lecture(lecturer2,'C++',8)
student1.rate_lecture(lecturer2,'Python',10)
student2.rate_lecture(lecturer2,'Git',9)

print('Лектор1:')
print(lecturer1)
print("Лектор1 в классе Ментор -> ", isinstance(lecturer1, Mentor))
print('')
#print(f'Оценки за лекции: {lecturer1.grades}\n')
print('Лектор2:')
print(lecturer2)
print("Лектор2 в классе Ментор -> ", isinstance(lecturer2, Mentor))
print('')
#print(f'Оценки за лекции: {lecturer2.grades}\n')
print(f'Лектор1, ср. оценка: {lecturer1._average_grade()} < Лектор2, ср. оценка: {lecturer2._average_grade()} -> {lecturer1 < lecturer2}')
print(f'Лектор1, ср. оценка: {lecturer1._average_grade()} = Лектор2, ср. оценка: {lecturer2._average_grade()} -> {lecturer1 == lecturer2}')
print(f'Лектор1, ср. оценка: {lecturer1._average_grade()} > Лектор2, ср. оценка: {lecturer2._average_grade()} -> {lecturer1 > lecturer2}\n')

print(f"Средняя оценка всех лекторов в рамках курса Python: {lecturers_average_grade([lecturer1, lecturer2], 'Python')}\n")
print('-' * 50)

reviewer1 = Reviewer('Петр', 'Петров')
reviewer1.courses_attached+=["C++", "Git"]
reviewer2 = Reviewer('Николай', 'Николаев')
reviewer2.courses_attached+=["Python", "Java"]
print('Эксперт1:')
print(reviewer1)
print('Эксперт2:')
<<<<<<< HEAD
print(reviewer2)
=======
print(reviewer2)    
>>>>>>> 3f80f56f78a2f32c07f3fa946dfd187ec58f5dc0













