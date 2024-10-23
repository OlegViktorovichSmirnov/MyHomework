# Словари и множества
#
# Цель: Написать программу на языке Python, используя Pycharm, для работы со словарями и множествами.
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.
#
# 2. Работа со словарями:
#  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
#  Например: Имя(str)-Год рождения(int).
#  - Выведите на экран словарь my_dict.
#  - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#  - Выведите на экран словарь my_dict.
#
# 3. Работа с множествами:
#  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#  - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#  - Удалите один любой элемент из множества my_set.
#  - Выведите на экран измененное множество my_set.

# Создаём словарь, имена неизменяемые, а вот ключи (значения) могут быть изменены

my_dict = {'Alex': 1835, 'Oliver': 2003, 'Agatha': 1974}
print(my_dict)
print(my_dict['Alex'])
my_dict['Martha'] = 2005
print(my_dict)

# Добавление несуществующих элементов

my_dict['Margaret'] = 1675
my_dict['Den'] = 1984
print(my_dict)

# Удаление элемента 'Den'

del my_dict['Den']
print(my_dict)

print(my_dict['Margaret'])
print(my_dict)

# Множество - остаточно полезный тип данных и тоже представляет собой некую коллекцию. Особенность множеств в том, что эта коллекция хранит уникальные значения.

my_set = {1756, 7.5, 'If Your body falls just get up, if You fall in sins cleanse them in Church', True, 'and again its', False, True, True}
print(my_set)

# Добавляем 2 несуществующих элемента
my_set.update({'Donald': 1345, 'Kamala': 1409})
print(my_set)

# Удаляем элемент 'Kamala'
print(my_set.discard('Kamala'))
print(my_set)