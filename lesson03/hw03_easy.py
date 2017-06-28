# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math


#def my_round(number, ndigits):
    #round = str(number).split('.')
    #if ndigits==0:
        #if int(round[1][0])<=5:
            #round[1]='0'
            #round='.'.join(round)
            #return int(float(round))

        #elif int(round[1][0])>5:
            #round[1]='0'
            #round[0]=str(int(round[0])+1)
            #round='.'.join(round)
            #return int(float(round))
    #else: 
        #round[1]=round[1][:ndigits]   
        #round='.'.join(round)
        #return float(round)

#print(my_round(0.6353454446456, 4))
#print(my_round(2.523456798345365, 0))
#print(my_round(2.1233534534454567, 10))


# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number1=list(str(ticket_number)[:3])
    ticket_number2=list(str(ticket_number)[3:])
    sum1 = sum(list(map(lambda number: int(number), ticket_number1)))
    sum2 = sum(list(map(lambda number: int(number), ticket_number2)))
    return sum1 == sum2
    

print(lucky_ticket(123321))

