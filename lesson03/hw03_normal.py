# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    farray = [1,1]
    for i in range(m-2):
        farray.append(farray[-1]+farray[-2])
    return farray[n-1:m]
    
print(fibonacci(5, 9))

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()


def sort_to_max(origin_list):
    n = 1 
    while n < len(origin_list):
         for i in range(len(origin_list)-n):
              if origin_list[i] > origin_list[i+1]:
                   origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
         n += 1    
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter

numbers = [1, 2, 3, 4, 5]


def filt(function, *args):
    args = args[0]
    new_array=[]
    for i in args:
        if function(i) == True:
            new_array.append(i)
    return new_array
            
even = filt(lambda x: x=='a', ['a', 'b', 'c', 'a'])
print(list(even))            

    


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

