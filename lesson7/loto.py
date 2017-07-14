#!/usr/bin/python3
'''
Лото
Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    - 43 62          74 90
 2    27    75 78    82
   41 56 63     -      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

* доп. задание
сделать так, чтобы можно было выбирать типы игроков (комп-комп, комп-чел, чел-чел)

'''
import random
class Card:
    def __init__(self):
        self.track0 = []
        self.track1 = []
        self.track2 = []

    def empty_in_line(self):
        empty = []
        while len(empty)<4:
            a = random.randint(0, 8)
            if a not in empty:
                empty.append(a)
        return sorted(empty)

    def add_line(self):
        random_numbers = []
        while len(random_numbers) < 27:
            a = random.randint(1, 90)
            if a not in random_numbers:
                random_numbers.append(a)
        #print(random_numbers, len(random_numbers))

        self.track0=(random_numbers[:9])
        empty = self.empty_in_line()
        for i in empty:
            self.track0[i] = ' '

        self.track1 =(random_numbers[9:18])
        empty = self.empty_in_line()
        for i in empty:
            self.track1[i] = ' '

        self.track2 =(random_numbers[18:27])
        empty = self.empty_in_line()
        for i in empty:
            self.track2[i] = ' '

    def new_card(self, name):
        text = ''
        if name == 'my_card':
            text = '------ Ваша карточка -----'
        elif name == 'comp_card':
            text = '-- Карточка компьютера ---'
        self.add_line()
        print("{0}\n{1}\n{2}\n{3}".format(text, self.track0, self.track1, self.track2))
        return [self.track0, self.track1, self.track2]

class Keg:
    def __init__(self):
        self.kegs = [ i for i in range(90)]

    def add_kegs(self):
        random.shuffle(self.kegs)
        return self.kegs
    def __getitem__(self, item):
        return self.kegs[item]
    def __len__(self):
        return len(self.kegs)


class Game:
    def __init__(self, card1, card2, kegs):
        self.card1 = card1
        self.card2 = card2
        self.kegs = kegs

    def run(self):

        for i in self.kegs:
            if (self.card1[0].count('-') < 5) and (self.card1[1].count('-') < 5) and (self.card1[2].count('-') < 5):

                respond = input('выпало число {}, зачеркнуть ?'.format(i))
                if ((i in self.card1[0]) or (i in self.card1[1]) or (i in self.card1[2]))and respond == 'y':
                    if i in self.card1[0]:
                        a = self.card1[0].index(i)
                        self.card1[0][a] = '-'
                    elif i in self.card1[1]:
                        a = self.card1[1].index(i)
                        self.card1[1][a] = '-'
                    elif i in self.card1[2]:
                        a = self.card1[2].index(i)
                        self.card1[2][a] = '-'
            else: print('Ты просто победитель по жизни!')
            print("{0}\n{1}\n{2}".format(self.card1[0], self.card1[1], self.card1[2]))




kegs = Keg()
new_kegs = kegs.add_kegs()
print(len(new_kegs))

cards = Card()
#new_card.new_card('my_card')
my_card = cards.new_card('my_card')
comp_card = cards.new_card('comp_card')
new_game = Game(my_card, comp_card, new_kegs)
new_game.run()






