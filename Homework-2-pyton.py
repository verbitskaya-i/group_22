import random
#1) Создать 2 переменных типа String с разными значениями.
name_1 = str(662)
name_2 = str(14)


#2) Создать 4 переменных типа Integer с разными значениями.
like_1 = int(17.2)
like_2 = int(1.8)
like_3 = int(10.9)
like_4 = int(4.1) 


#3) Создать 3 переменных типа Float с разными значениями.
good_1 = float(85)
good_2 = float(20)
good_3 = float(64)


#4) Реализовать 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
print(like_1 > like_2)
print(like_1 < like_3)
print(like_1 >= like_3)
print(like_1 <= like_2)
print(like_1 != like_2)
print(like_2 > like_1)
print(like_2 < like_3)
print(like_2 >= like_3)
print(like_2 <= like_1)
print(like_2 != like_3)
print(like_3 > like_1)
print(like_3 < like_4)
print(like_4 != like_3)
print(like_4 >= like_2)
print(like_4 <= like_1)

#5) Реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
print(good_1 > good_3)
print(good_1 < good_2)
print(good_1 >= good_3)
print(good_2 <= good_1)
print(good_2 != good_3)
print(good_2 > good_3)
print(good_3 < good_1)
print(good_3 >= good_2)
print(good_3 != good_1)

 
#6) Реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.

if like_1 > 19 or like_2 < 10: #or - один оператор должен быть "True" (т.е равняться 1)
      print("like_1 не больше 19, like_2 < 10")
if like_3 > 15 or like_1 >= 12:
      print("like_3 не больше 15, like_1 >= 12")
if like_4 <= 6 or like_1 >= 18:
      print("like_4 <= 6, like_1 не больше либо равно 18")
if like_3 != 15 or like_2 < 25:
      print("like_3 не равно 15, like_2 < 25")
if like_2 >= 1.8 and like_1 != 17.2: #and - все операторы должны быть "True" (т.е равняться 1)
      print("True")
if like_4 != 62 and like_3 > 8:
      print("Yes, like_4 not 62 and like_3 more 8")
if like_3 = 10.9 and like_4 < 3:
      print("True")
if not like_1 > 118: #not - один оператор должен быть "False" (т.е равняться нулю)
      print("like_1 не больше 118")
if not like_3 <= 5:
      print("Нет, like_3 не больше либо равно 5")
if not like_4 < 3:
      print("like_4 не меньше 3""\n")


#7) Сделать скрипт используя функцию input().
#   1. Функция должна на вход принимать целое число.
#   2. Выводить должна "Вы ввели число = (введенное число), которое (меньше/больше/равно) 30".

a = int(input()) 
if a < 30:
      print("you entered a number " + str(a) +  " that is less than 30")
elif a > 30:
      print("you entered a number " + str(a) + " that is greater than 30")
elif a == 30:
      print("you entered a number " + str(a) + " that is equal to 30")
else:
      print("Error!a")


#8) Сделать скрипт используя функцию input().
#   1. Функция должна на вход принимать целое число.
#   2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100)).
#   3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу" .

b = int(input()) 
import random
if b < 20:
      print("you entered a number " + str(b) + " that is less than " + str(random.randint(1, 100)))
elif b > 50:
      print("you entered a number " + str(b) + " that is greater than " + str(random.randint(1, 100)))
elif b == 87:
      print("you entered a number " + str(b) + " that equals " + str(random.randint(1, 100)))
else:
      print("Error!b")


#9) Сделать скрипт используя функцию input().
#   1. Функция должна на вход принимать целое число.
#   2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100)).
#   3. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу".

UserVar = int(input())
RandomOne = int((random.randint(1, 100)))
RandomTwo = int((random.randint(1, 100)))

if UserVar > RandomOne and UserVar > RandomTwo: 
      print("Вы ввели число " + str(UserVar) + " которое больше " + str(RandomOne)+ " и больше " + str(RandomTwo))

elif UserVar < RandomOne and UserVar < RandomTwo: 
      print("Вы ввели число " + str(UserVar) + " которое меньше " + str(RandomOne)+ " и меньше " + str(RandomTwo))

elif UserVar > RandomOne and UserVar < RandomTwo: 
      print("Вы ввели число " + str(UserVar) + " которое больше " + str(RandomOne)+ " и меньше " + str(RandomTwo))

elif UserVar < RandomOne and UserVar > RandomTwo: 
      print("Вы ввели число " + str(UserVar) + " которое меньше " + str(RandomOne)+ " и больше " + str(RandomTwo))

elif UserVar == RandomOne and RandomTwo: 
      print("Вы ввели число " + str(UserVar) + " которое равно " + str(RandomOne) + "и равно" + str(RandomTwo))
else:
      print("Error!")
