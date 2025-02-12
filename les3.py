import math


# 1. Есть три целочисленные переменные, нужно посчитать:
# сумму
# разность
# произведение
# от первой переменной отнять вторую и прибавить третью
# поделить произведение двух переменных на третью
# от суммы первых двух переменных найти остаток от деления на третью переменную

a = 25
b = 13
c = 4


amount = a + b + c
print(amount)

difference = a - b - c
print(difference)

work = a * b * c
print(work)

difference = (a - b) + c
print(difference)

work_a = (a * b) / c
print(work_a)

amount_a = (a + b) % c
print(amount_a)


# 2. Дан прямоугольный треугольник с катетами cat_a и cat_b.
# Найти площадь треугольника и его гипотенузу.
cat_a = input('cat_a = ')
cat_b = input('cat_b = ')

cat_a = float(a)
cat_b = float(b)

area = (a * b) / 2
hypotenuse = math.sqrt(a**2 + b**2)
perimeter = a + b + c

print('Area:', area)
print('Perimeter:', round(perimeter, 2))


# 3.Дана строка, состоящая из слов, разделенных пробелами.
# (Вот 4 варианта тестовых данных для программы:
# ‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’).
# Определите, сколько в ней слов.


text = ('‘Hello world’, ‘a b c’, ‘test’, ‘test1 test2 test3 test4 test5’')
print(text.count(' ') + 1)


# 4. Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения. Подсказка: использовать метод replace
# с параметрами. Например, дано: ‘hhhabchghhh’, должно быть: ‘hHHabcHgHHh’

line = ('hhhabchghhh')
print(line.replace('h', 'H', line.count('h')-1).replace('H','h',1))


# 5. Дана строка.
# 1 Сначала выведите третий символ этой строки.
# 2 Во второй строке выведите предпоследний символ строки.
# 3 В третьей строке выведите первые пять символов строки.
# 4 В четвертой выведите всю до последних двух символов.
# 5 В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# 6 В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# 7 В седьмой строке выведите все символы в обратном порядке.
# 8 В восьмой строке выведите все символы строки через один в обратном порядке,
# начиная с последнего.
# 9 В девятой строке выведите длину данной строки.

string = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNn'
print(string[2])
print(string[-2])
print(string[:5])
print(string[:-2])
print(string[::2])
print(string[1::2])
print(string[::-1])
print(string[::-2])
print(len(string))


# Тестовые данные для 5 задачи:
# строка ‘Hello’, должно быть:
# l
# l
# Hello
# Hel
# Hlo
# el
# olleH
# olH
# 5


string = 'Hello'
print(string[2])
print(string[3])
print(string[:5])
print(string[:3])
print(string[::2])
print(string[1:3])
print(string[::-1])
print(string[::-1])
print(string[::-2])
print(len(string))


# Дано целое число. Выведите его последнюю цифру.
# Например, дано 200 - последняя цифра 0. Дано 123 - последняя цифра 3. Дано 587 - последняя 7.

number_one = 200
number_two = 123
number_tree = 587

print(number_one % 10)
print(number_two % 10)
print(number_tree % 10)


# 7. Дано трехзначное число, найти количество его десятков. Например, дано 123 – количество десятков: 2,
# дано 978 – количество десятков: 7.

number_one = 123
number_two = 978
print(number_one // 10 % 10)
print(number_two // 10 % 10)


# 8. Дано трехзначное число, найти сумму его цифр. Например, дано 123 – сумма 6, дано 555, сумма 15.

number_one = 123 // 100
number_two = 123 // 10 % 10
number_tree = 123 % 10
print(number_one + number_two + number_tree)

number_one = 555 // 100
number_two = 555 // 10 % 10
number_tree = 555 % 10
print(number_one + number_two + number_tree)