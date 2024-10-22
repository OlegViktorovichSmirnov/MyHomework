# Практическая работа по уроку "Организация программ и методы строк."
#
# Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.
#
# 1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_6.py' и напишите весь код в нём.
#
# 2. Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести количество символов введённого текста
#
# 3. Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.
#
# Примечания:
#
# Для вывода значений на экран используйте функцию print().
# Для вызова методов строк используйте операцию точки '.'.

# Запрос ввода произвольного текста

my_string = input('Введите текст: ')

# Ввод текста в верхнем регистре

print(my_string .upper())

# Ввод текста в нижнем регистре

print(my_string .lower())

# Вывод текста заменив все пробелы на "#"

print(my_string .replace(' ', '#'))

# Вывод первого символа

print(my_string[0])

# Вывод последнего символа

print(my_string[-1])