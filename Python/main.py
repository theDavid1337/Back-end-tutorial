# -*- coding: utf-8 -*-

"""
    Introduction to Python 3
    Editor VS code
    Learn python : 3


    LESSON 1
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    --------------------------------------------------------------------------------------------------
    LESSON 2
    Dastur tushunchasi
    Variable
    Math
    Data types
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    -------------------------------------------------------------------------------------------------- 
    LESSON 3
    Operators
    If Else
    Tasks
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    -------------------------------------------------------------------------------------------------- 
    LESSON 4
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    -------------------------------------------------------------------------------------------------- 
    LESSON 5
    Integers
    Strings
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    -------------------------------------------------------------------------------------------------- 
    LESSON 6
    Strings
    Symbols
    --------------------------------------------------------------------------------------------------
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    --------------------------------------------------------------------------------------------------
"""

# import locale
# import calendar
# locale.setlocale(locale.LC_ALL, 'uz_Uz')

# Lesson 1
# Python Indent Extention

# print('Hello World !') # Showing result

# Interpritator - kodni tori yozilganini teshiruvchi dastur
# Compilator - kodni mashina tiliga o'giruvchi dastur

# Lesson 2
# print "String 2" # Python 2
# print('String 3') # Python 3

# Dastur :
#           1 - Malumot qabul qiladi >>> input()
#           2 - Uni qayta ishledi >>> +-*/
#           3 - Saqlaydi >>> Ozgaruvchilar
#           4 - Natijani qaytaradi


# RAM = Random Access Memory


# def main():
#     return 10

# print(main)  # <function main at 0x000001AA5CFC3E20>

# name = "name"
# print(name)

# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# user = 'gandi'
# User = 'Mahatma'
# USER = 'gandi' // const
# _user = 'Chaplin'
# print(user)  # gandi
# print(User)  # Mahatma
# print(_user)  # Chaplin

# userProfilePhotoUrl = 'img/photo.png'  # Camel Case : Javascript
# user_profile_photo_url = "img/photo.png"  # Snake Case : Python


# Python Data Types

# Numbers
# int - butun son >>> 1, -1, 0
# float - qoldiq son >>> 1.1 2.1
# complex - 2n

# Strings
# str - qator >>> "", '', """"""

# Booleans
# bool - Boolean turi >>> True, False

# None
# none - Qiymati mavjud emas >>> None

# Butes
# bytes - baytlar qiymati >>> 1, 0
# bytearray - baytlar massivi
# list - royhat turi, o'zgaruvchan tartibli elementlar toplami >>> [1, 2, 3]
# tuple - kortej , o'zgarmas tartibli elementlar to'plami
# range - diapazon , sonlar oralig'i
# dict - dictionary - lug'at , kalit va qiymatlarga kalit orqali murojaat qilinadigan elementlar toplami
# set - tartibsiz , unikal elementlar toplami
# frozenset - tartibsiz , o'zgarmas , unikal elementlar toplami

# num = 10
# print(type(num))  # <class 'int'>
# num = 10.1
# print(type(num))  # <class 'float'>


# x, y, z = 1, 2, 3
# print(x)  # 1
# print(y)  # 2
# print(z)  # 3


# a = 10
# b = 20
# a, b = b, a
# print(a)
# print(b)


# str_num = "10"
# print(type(str_num))  # <class 'str'>
# print(int(str_num) + 5)
# print(str_num * 2)

# user_input = int(input("Son kiriting : "))
# user_input = float(input("Son kiriting : "))
# user_input = str(input("Matn kiriting : "))

# x = 0
# del x
# print(x)

# print(2 + 2)  # 4
# print(2 - 1)  # 1
# print(2 * 3)  # 6
# print(2 ** 3)  # 8
# print(10 / 5)  # 2.0 Bolib qoldiq omoqchi bolsa
# print(10 // 5)  # 2 Bolib qoldiqsiz omoqchi bolsa
# print(10 % 3)  # 1 Bolganda qoldiqni chiqarish

# s = 'python'
# print('yth' in s)  # True
# print('va' in s)  # False

# print('vakakavaka' not in s)  # True


# Qoshib tenglash
# num = 0
# num += 1
# num += 1
# print(num)  # 2


# Ayrib tenglash
# num = 4
# num -= 1
# num -= 1
# print(num)


# Qarra qilib tenglash
# num = 2
# num *= 2
# num *= 2
# print(num)


# Bo'lib tenglash
# num = 10
# num /= 2 # 5.0
# num //= 2 # 5
# print(num)

# Logical operators

# print(10 == 100)  # False
# print(10 == 10)  # True
# print(10 != 10)  # False
# print(10 != 10)  # False
# print(10 != 10.0) # False
# print(3 > 4)  # False
# print(3 >= 4)  # False
# print(3 <= 4)  # True


# y = [1, 2]
# x = y
# print(x is y)  # True

# a = 'a'
# b = 'b'

# print(a is b)
# print("a" is not "b")

# print(1 < 2 and 1 < 5 and 8 <= 30)  # True


# print(1 > 0 or 1 == 0)  # True
# print(1 < 0 or 1 == 0)  # False

# Operators with letter
# in , is , not , not in , is not , and , or

# print(not True) # False
# print(not False)  # True

# print(not 0) # True
# print(not " ") # False


# if 1 > 0:
#     print("IF")
# elif 1 > 0:
#     print("ELIF")
# else:
#     print('ELSE')


# user = input()
# if user.isalpha():
#     if "olma" == user:
#         print('Olma Topildi')
#     else:
#         print('Olma Yoq')
# else:
#     print('Iltimos matn kiriting !')


# Task 1
# p = 2
# print(4 * p)


# Task 2
# s = 2
# print(s ** s)


# Task 3
# a = 2
# b = 3
# s = a * b
# print(s)
# p = 2 * (a + b)
# print(p)


# Task 4
# d = 10
# p = 3.14
# l = d * p
# print(l)


# Task 5
# a = 5
# v = a ** 3
# s = 6 * a ** 2
# print(v, s)


# Task 6
# a = 2
# b = 3
# c = 5
# v = a * b * c
# s = 2 * (a * b + b * c + c * a)
# print(v, s)


# Task 7
# r = 6
# l = 2 * 3.14 * r
# s = 3.14 * r ** 2
# print(l, s)


# Task 8
# a = 4
# b = 5
# print((a + b) / 2)


# Task 9
# a = 3
# b = 3
# print((a * b) ** 0.5)


# Task 10
# a = 5
# b = 6
# print(a + b)
# print(a * b)
# print(a ** a)
# print(b ** b)


# Task 11 ?

# Task 12
# a = 10
# b = 5
# c = a + b
# p = a + b + c
# print(c, p)


# Task 13
# r1 = 12
# r2 = 9
# s1 = 3.14 * r1
# s2 = 3.14 * r2
# s3 = 3.14 * (r1 - r2)
# print(s1, s2, s3)


# Task 14

# Task 15

# Task 16
# x1 = 10
# x2 = 20
# print(x2 - x1)


# Task 17
# a = 10
# b = 15
# c = 8

# print(a + c, a + b)


# Realniy Task 1
# user_first_num = 1
# user_second_num = 5

# if user_first_num % 2 == 1 and user_second_num % 2 == 1:
#     print(user_second_num + user_first_num)
# elif user_first_num % 2 == 0 or user_second_num % 2 == 0:
#     print(user_first_num * user_second_num)
# else:
#     print(0)


# Task 2
# first = 4
# second = 2
# third = 3
# if first > second and first > third:
#     print(first)
# elif second > first and second > third:
#     print(second)
# else:
#     print(third)


# Task 3
# first_surname = "Valuev"
# second_surname = "Karimova"
# third_surname = "Ulugbekova"
# men = 0
# women = 0
# if first_surname.endswith('v'):
#     men += 1
# else:
#     women += 1

# if second_surname.endswith('v'):
#     men += 1
# else:
#     women += 1

# if third_surname.endswith('v'):
#     men += 1
# else:
#     women += 1

# print('Men', men, 'Women', women)


# Lesson 5

# int () 1.2 >> 1
# print(int("1.2"))
# print(int('1') + 2)

# float() >> 1 >> 1.0 -> bunga faqat son bersa bo'ladi
# print(float('1.2') + 1.2) ----> hotya string bilan ishlasa bo'ladi


# print(bin(1)) --> # 0b1010
# print(oct(10)) --> # 0o12
# print(hex(10)) --> # 0xa

# print(round(12.2)) # 12
# print(round(12.6)) # 13 Yaxlidlash

# print(abs(-12))  # 12 Modul

# print(pow(5, 3)) # 125 >> 5 ** 3

# print(max([1, 2, 3]))  # Eng kattasini chiqaradi ->> 3
# print(min([1, 2, 3]))  # Eng qichkinasini chiqaradi ->> 1
# print(sum([1, 2, 3])) # Ularning summasini chiqaradi ->> 6

# n = 10.0
# # True >>> Butun qilih imkoniyati bormi, esli da to mojno sdelat ego int
# print(n.is_integer())  # True
# n = 10.2
# print(n.is_integer())  # False


# import math
# import random

# print(math.pi)  # 3.141592653589793

# print(math.ceil(12.6))  # 13
# print(round(12.6))  # 13
# print(math.floor(12.9))  # 12

# print(round(random.random() * 10))
# Ikkta sonni orasidagi tasodifiy son >>> (start, stop)
# print(random.randint(0, 10))


# # Ketma-ketlikdan tasodifiy bitta elementni olish
# print(random.choice('python'))
# # Ketma-ketlikdan tasodifiy bir nechta element ni olish
# print(random.sample('python', 2))

# arr = [1, 2, 3, 4, 5]
# random.shuffle(arr)
# print(arr)

# print(random.shuffle([1, 2, 3, 4, 5]))


# Task 1


# first_num = int(input())
# second_num = int(input())

# if second_num >= 6:
#     for count in range(first_num):
#         for k in range(first_num):
#             text = random.sample("1234567890-=!@#$%^&*()_+", second_num)
#         output = ''
#         for i in text:
#             output += i
#         print(output)
# else:
#     print('Not working...')


# v 2.0
# letter_low = 'qwertyuiopasdfghjklzxcvbnm'
# letter_up = letter_low.upper()
# symbols = '!@#$%^&*()'

# chars = letter_low + letter_up + symbols

# pass_count = int(input('Count ? \n'))
# letters_count = int(input('Count ? \n'))

# if letters_count >= 6:
#     for i in range(pass_count):
#         password = ""
#         for l in range(letters_count):
#             password += random.choice(chars)
#         print(password)


# word = "yangi o'zbekiston"
# letter = "svet"

# counter = 0
# for char in word:
#     for i in letter:
#         if char == i:
#             counter += 1
# print(counter)

# print(len(''.join([x for i in "svet" for x in "yangi o'zbekiston" if i == x])))

# print()
# user_input = int(input('Number ? \n'))
# counter = 0
# for i in range(100):
#     random_num = random.randint(0, 100)
#     if user_input == random_num:
#         counter += 1
# print(counter)


# Task 4
# for num in range(x, y):
#     print(num)


# Task 5
# x = 2
# y = 5
# sum_num = 0
# expose_num = 0
# for num in range(x, y + 1):
#     print(num, pow(num, 2))
#     sum_num += num
#     expose_num += pow(num, 2)
# print(sum_num)
# print(expose_num)


# x = 10
# print(True) if x > 5 else print(False)

# # If - Block Condition Else - Block
# print('Yes' if 10 % 2 == 0 else 'No')

# if x > 20:
#     l = 0
#     print('yes')
# else:
#     print('no')
# print(l)


# Loops
# for while
# while - toxtovsiz sikl

# for - sanoqli sikl, boshqarildigon

# for sikli - ketma-ketlilar bilan ishlaydi

# for i in 'python':
#     print(i)

# for i in range(1,6):
#     print(i)
# print(type(range(1, 6)))
# print(dir(range(1, 6)))

# range - 'start', 'step', 'stop'
# start = 1
# step = 2
# stop = 15
# for i in range(start, stop, step):
#     print(i)
# print(list(range(start, stop, step)))

# Agar range bitta arg qabul kilsa u stop boladi


# for k in 'stars':
#     print(type(k))
#     print(k)

# for i in input():
#     if i == 'a':
#         print('yes')

# for x in range(10):print(x)

# def main(num):
#     return num ** num
# for x in range(10): print(main(x))

# s = 'Python is n1'
# for i in enumerate(s):
#     print(i) # (0, 'P')

# for i in range(5):
#     if i % 2 == 0:
#         print(i)
# else: # sikl ohiridagi amallar uchun
#     print('Loop Tugadi')


# s = 5
# for i in range(s):
#     print(i)
# else:
#     s = 100


# i = 0

# while True:
#     i += 1
#     if i % 10000000 == 0:
#         print('While')

# yeild

# condition = True
# while condition:
#     user_input = input()
#     if user_input == 'gandi123':
#         print('Xush Kelibsiz!')
#         # condition = False
#         break # bu siklni majburiy toxtatish
#     else:
#         # condition = True
#         continue # keyingi siklga o'tish
# condition = True
# user_num = 0

# while condition:
#     user_input = input()
#     if user_input.isdigit():
#         number = int(user_input)
#         user_num += number
#     if user_input == 'stop':
#         condition = False
#         print(user_num)


# Task
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# user_input = input()
# # for letter in enumerate(alphabet):
# #     if user_input == letter[1]:
# #         print(letter[0] + 1)
# output = 0
# condition = True
# while condition:
#     user_num = input('Write...')
#     if user_num == 'stop':
#         condition = False
#     else:
#         if len(user_num) == 2 and int(user_num) % 10 == 0:
#             user_num = int(user_num)
#             output += user_num
# print(output)


# str = '1  24 1 51 2 51 5 sg d sg s dg dsg '
# str.removeprefix(' ')
# print(str)


# print('hello \n world New line')
# print('hello \t world Tab')

# print('\a')
# print(r'hello \n world but not in new Line') # hello \n world but not in new Line

# print("\U0001f604")

# print('\\')


# s = "bu 'qora' olma"
# print(s)
# s = 'bu "qora" olma'
# print(s)
# print(s[-1])

# print(s[len(s) - 1])

# CONCAT

# s = 'Rubi on rails'
# on = s[0:4] # R , u , b , i
# print(on) # Rubi
# print(len(on)) # 4

# print(s[:4])
# print(s[5:7]) # Cut, from index, to index
# print(s[8:])
# print(s[:]) # String copy

# print('kitob'[::-1]) # botik


# age = 30
# name = "John Doe"

# user = "name = %s, age = %s" %(name, age) # name = John Doe, age = 30
# print(user)

# user = "name = {0}, age = {1}".format(name,age) # name = John Doe, age = 30

# user = f"name = {name}, age = {age}" # name = John Doe, age = 30
# print(user)


# s = ' hay,hayr,qale '
# print(len(s))
# print(len(s.strip()))
# print(len(s.rstrip()))
# print(len(s.lstrip()))

# print(s.split(','))


# print('Python'.upper())
# print('Python'.lower())
# print('python'.capitalize())
# print('Python'.swapcase())
# print('python'.title())
# print('python'.find('on'))
# print('Python is better'.rfind('b'))
# print('Python is better'.index('bet'))
# print('on table on table'.count('on'))
# print('aloha chicas'.replace('chicas','muchachos'))
# print('gandi'.startswith('gan')) # True
# print('gandi'.endswith('gan')) # False

# user_input = 'lkjlg;kajlk;gjaklg,gazimiz svetacopy gaz svetlar yoq'.lower().split(' ')
# arr = ['gaz','svet','yoq']
# print(len([x for i in arr for x in user_input if i == x]))


# s = '12.0'
# print(s.isdigit()) # True
# print("1825jhgkjs".isalnum()) # isalnum - is alphabet numeric
# print(s.isalpha()) # False
# print("AA".isupper()) # True
# print("Not lower".islower()) # False
# print("Aa".istitle()) # True

# password:
#     - minimum 6 ta belgi
#     - kamida bitta katta harf
#     - kamida bitta maxsus belgi (/ , \ , @ , _ , -)
#     - kamida bitta butun son


# user_input = input()
# upper_str = 0
# symbols = 0
# number = 0
# symbols_arr = ["/", "@", "_", "-"]
# if len(user_input) >= 6:
#     for i in user_input:
#         if user_input[i].isdigit():
#             number + 1
#         if user_input[i].isupper():
#             upper_str + 1
#         for i in symbols:
#             if user_input[i] == symbols[i]:
#                 symbols + 1
#     if upper_str >= 1 or symbols >= 1 or number >= 1:
#         print('Your Pass is True')
#     else:
#         print("Your Pass is False \nTry again")
# else:
#     print("Pass less than 6")


# password = 'Aaklslvak_1337'

# upper_letter = False
# digit = False
# symbols = False

# if len(password) >= 6:
#     for letter in password:
#         if letter.isdigit():
#             digit = True
#         if letter.isupper():
#             upper_letter = True
#         if letter in "/\\@-_":
#             symbols = True
#     if upper_letter and digit and symbols:
#         print('Password is True')
#     else:
#         print('Password is False')
# else:
#     print('Password less than 6')


# NEW LESSON

# l = list()
# l = [1,"number",[1,2,3]]
# # print(l[0]) # 1
# # print(len(l[2])) # 3

# l.append('appended element')
# print(l) # [1, 'number', [1, 2, 3], 'appended element']

# append - oxiriga qoshish
# pop - oxiridan o'chirish
# index - elementni indexini olish
# insert - index orqali elementni qoshish
# reverse - elementlar indexini teskari qilish
# count - list da elementni takrorlanishini sanash
# sort - saralash
# remove - elementni ochirish
# extend - boshqa massiv bilan kengaytirish
# copy - list nusxasini olish
# del l[index] - elementni ochirish
# clear - listni tozalash

# x,y = 1,2
# print(x + y)

# x , y , *z = [1 , 2 , 3 , 4 , 5 , 6] # -> x = 1, y = 2, z = [3 , 4 , 5 , 6]


# *args - , **kwars

# def check_user(*args):
#     for i in args:
#         print(i)

# check_user('Hello',12,True,'Bla Bla Bla')

# arr = [1,2,3,4,5]

# print(arr[:]) # [1,2,3,4,5]
# print(arr[3:]) # [4,5]
# print(arr[2:3]) # [3]

# arr.reverse()
# print(arr)

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# def check_user(*args):
#     for i in args:
#         print(i)

# check_user(arr)

# for i in arr:
#     for k in i:
#         print(k)


# user_input = 'qovun'
# output = ''
# user_list = []

# for i in user_input:
#     user_list.append(i)
# first_char = user_list[0]
# last_char = user_list[-1]

# user_list[0] = last_char
# user_list[-1] = first_char

# for i in user_list:
#     output += i
# print(output)

# arr = [1, 2, 3, 4, 5]
# # l = [i**2 for i in arr]
# # print(l)
# l = [i**2 for i in arr if i % 2 == 1]
# print(l)


# arr = [[1, 2], [3, 4], [5, 6]]
# new_arr = [j * 10 for i in arr for j in i if j % 2 == 0]
# print(new_arr)

# Task 3

# user_input = 'ahg;kjasghkjasgha;sgkasgka;skg;alskg;laskglkaskgaojgaAGagags'
# print([char for char in user_input if char.lower() == 'a'])


# def main(num):
#     return num + 5


# arr = [1, 2, 3, 4, 5]
# print(map(main, arr))  # <map object at 0x0000023CF94EADA0>
# print(list(map(main, arr)))  # [6, 7, 8, 9, 10]

# name = 'John'
# position = [1, 2, 3, 4]

# print(zip(name, position))  # <zip object at 0x000002A869C67840>
# print(list(zip(name, position)))  # [('J', 1), ('o', 2), ('h', 3), ('n', 4)]


# for x in list(zip(name, position)):
#     for i in x:
#         print(i, end="")  # J1o2h3n4


# alpha = "abcdefgh"
# print(list(zip(alpha, list(range(len(alpha))))))

# letters = list(zip(alpha, list(range(len(alpha)))))
# e = "e"

# for i in letters:
#     if e == i[0]:
#         print(i[1] + 1)


# a = "aaaaa"
# b = list(range(10))
# print(list(zip(a, b)))  # [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('a', 4)]

# def odd(n):
#     if n % 2 == 1:
#         return n


# arr = list(range(1, 11))
# print(list(filter(odd, arr))) # [1, 3, 5, 7, 9]


# Task 4

# l = [i**2 for i in arr if i % 2 == 1]
# new_arr = [j * 10 for i in arr for j in i if j % 2 == 0]
# a = [1, 2, 3, 4, 5]
# b = [2, 7, 7, 5, 3]

# print(item for i in a for item in b if i == item del item)
# for first_num in a:
#     for second_num in b:
#         if first_num == second_num:
#             x = a.index(first_num)
#             y = b.index(second_num)
#             del a[x]
#             del b[y]
# print(a, b)

# new_arr = []


# arr = [1, 2]
# print(2 in arr) # True
# # arr[:0] = [-2, -1, 0]
# # print(arr)

# arr. insert (2, 100); arr # Вставляем 100 в позицию 2
import random
# arr = [random.randint(1, 50) for x in range(10)]

# print(arr)

# reverse = Qamayish tartibi
# for i in sorted(arr,reverse=True):
#     print(i)

# print(sorted("aghakjsghajkgAG", key=str.upper, reverse=True))

# list 100 gacha sanoq boylab elementlar ni olish
# arr = list(range(10, 100, 10))
# print(arr)


# # arr = random.sample(range(100), Elements)
# # sample range 100 gacha bo'lgan 10 ta Tasodifiy element olish
# arr = random.sample(range(100), 10)
# print(arr)


# t = tuple()
# t = ()

# arr = [1, 2, 3]
# del arr[2]  # Success !


# t = (1, 2, 3)
# del t[2]  # TypeError: 'tuple' object doesn't support item deletion


# Supported methods >> min , max , count , index , [:] , [0] , len

# def main(*args):
#     print(type(args))
#     print(args)


# main(1, 2, 3, 4, 5, "gas", "asg", "asf", (1, 2, 3))


# s = set()
# s = {}
# # har doim har xil index kilib unique kilib beradi
# print(set('assalom'))  # {'s', 'a', 'o', 'm', 'l'}


# Supported methods >> len , add , remove

# fs = frozenset("assalom")
# Supported methods >>> No Methods
# print(fs)

# dict

# d = dict(name="John Doe", age=30)
# print(d)  # {'name': 'John Doe', 'age': 30}
# d = {
#     "name": "John",
#     "surname": "Doe",
#     "age": 20
# }
# print(d)  # {'name': 'John', 'surname': 'Doe', 'age': 20}

# print(d["name"])  # John
# print(d["money"])  # KeyError: 'money'
# print(d.get("name"))  # John - get_object_or_404 >> get or None
# print(d.get("money"))  # None


k = ["monkey", "elephant"]
v = [12, 5]
print(dict(zip(k, v)))  # {'monkey': 12, 'elephant': 5}
