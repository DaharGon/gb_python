# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Scool:
    def __init__(self):
        self.teachers = []
        self.classes = []

    def get_classes(self):
        for i in self.classes:
            all_classes = [i.room for i in self.classes]
            return all_classes

class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)


class Rate:
    def __str__(self):
        return self.room

    def __init__(self, room):
        self.room = room
        self.students = set()
        self.teachers = []
        sk.classes.append(self)

    def set_student(self, student):
        self.students.add(student)

    def get_students(self):
        return self.students

    def get_teachers(self):
        for i in sk.teachers:
            if (str(i.room) == str(self.room)):
                self.teachers.append('{} {}'.format(i.name, i.surname))
        return self.teachers


class Teachers(People):
    def __init__(self, name, surname, cours, room):
        People.__init__(self, name, surname)
        self.cours = cours
        self.room = room
        sk.teachers.append(self)


class Student(People):
    def __init__(self, name, surname, parent1, parent2, room):
        People.__init__(self, name, surname)
        self.parent1 = parent1
        self.parent2 = parent2
        self.room = room
        Rate.set_student(self.room, '{0} {1}'.format(self.name, self.surname))

    def get_courses(self):
        all_courses = [i.cours for i in sk.teachers if i.room == self.room]
        return all_courses

    def get_parrents(self):
        return '{0}, {1}'.format(self.parent1, self.parent2)



sk = Scool()
room1 = Rate('7D')
room2 = Rate('8R')
room3 = Rate('5Q')
teacher1 = Teachers('Алексей','Кузнецов','Математика',room1)
teacher2 = Teachers('Алекс','Кузнец','Информатика',room1)
teacher3 = Teachers('Ал','Куз','Биология',room2)
teacher4 = Teachers('Николай','Пузиков','Русский язык',room3)

stud1 = Student('Вася','Журавликов','Елена Константиновна','Виктор Сергеевич', room1)
stud2 = Student('Сергей','Болтунов','Милана Александровна','Андрей Геннадьевич', room1)
stud3 = Student('Ученик','Номер3','Елена Константиновна','Виктор Сергеевич', room3)

# 1. Получить полный список всех классов школы
print(sk.get_classes())
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
print(room1.get_students())
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
print(stud1.get_courses())
# 4. Узнать ФИО родителей указанного ученика
print(stud1.get_parrents())
# 5. Получить список всех Учителей, преподающих в указанном классе
print(room1.get_teachers())












