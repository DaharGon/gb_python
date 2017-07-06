
import re
import os
import sys
import shutil
# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#создаем
try:
    for i in range(1, 10):
        os.mkdir('dir_'+str(i))
except FileExistsError:
    print('Папка уже есть!')
#проверяем, удаляем

folders = os.listdir()
for folder in folders:
    r = re.search(r'dir_[0-9]', folder)
    if r is not None:
        os.rmdir(r.group())





# Задача-2:
# Напишите скрипт отображающий папки текущей директории




# Леонид, не могу понять, почему цикл проходит не по всем элементам ?
all_files = os.listdir(os.getcwd())
#print(all_files) #['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'hw05_easy.py', 'hw05_hard.py', 'hw05_normal.py']
for folder in all_files:
    if os.path.isdir(os.path.join(os.getcwd(), folder)):
        pass
    else:
        all_files.remove(folder)
print(all_files)#['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'hw05_hard.py']


# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

this_file = (sys.argv[0])
file_new = os.path.join(os.getcwd(), 'new_file.py')
shutil.copyfile(this_file, file_new)

