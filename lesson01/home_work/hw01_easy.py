# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

# код пишем тут...
a=input('Введи число')
for i in range(len(a)):
    print(a[i])

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это неправильное решение!
a=int(input('Введи число a'))
b=int(input('Введи число b'))
a, b = b, a
print(a)
print(b)

# Задача-3: Запросите у пользователя год рождения. Если ему есть 18 лет, выведите: "Доступ разрешени",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
age = int(input('Сколько тебе лет ?'))
if (age >= 18) :
    print("Доступ разрешени")
else: print("Извините, пользование данным ресурсом только с 18 лет")