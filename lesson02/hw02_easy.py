# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка выровненного по правой сторне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print('Задача 1')
fruts = ["яблоко", "банан", "киви", "арбуз", 'какой то неведомый фрукт']
max_len = float('-inf')
for frut in fruts:
    if len(frut)>max_len:
        max_len = len(frut)
ident = 0
i=1
for frut in fruts:

    if len(frut)<max_len:
        ident=max_len-len(frut)
    else: ident=0
    print('{item}. {iden} {fr}'.format(item=i, iden=ident*' ', fr=frut))
    i=i+1
print('*'*50)

# Подсказка: использует метод .format()

# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке
print('Задача 2')
len_sp1 = input('Введите количество слов в первом списке: ')
sp1 = set(input('Введите слова первого списка через пробел: ').split(' '))
len_sp2 = input('Введите количество слов во втором списке: ')
sp2 = set(input('Введите слова второго списка через пробел: ').split(' '))
print(sp1-sp2)
print('*'*50)
# Задача-3:
# Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного выполнив следующие условия:
# если элемент кратный двум, то разделить его на 4, если не кратен, то умножить на два.
print('Задача-3')
sp = input('Введите числа через пробел: ').split(' ')
sp_new = []
for i in sp:
    if (int(i)%2==0):
        sp_new.append(int(i)/4)
    else: sp_new.append(int(i)*4)
print(sp_new)
