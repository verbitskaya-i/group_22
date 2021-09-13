# 1-9) Создать переменные.
variable_1 = str(10) #строки string 
variable_2 = int(15.7) #целое число integer
variable_3 = float(10) #число с плавающей точкой
variable_4 = bytes(17) #байты
variable_5 = list("Python") #список
variable_6 = tuple("Hello") #кортедж
variable_7 = set("variable_7") #множество
variable_8 = frozenset("variable_8") #неизменяемое множество
variable_9 = dict( [ (1,2), (3,4) ] ) #словарь


#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(str(variable_1)) 
print(int(variable_2))
print(float(variable_3))
print(bytes(variable_4))
print(list(variable_5))
print(tuple(variable_6))
print(set(variable_7))
print(frozenset(variable_8))
print(dict(variable_9))


#11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
balance = str(10)
deposit = str(5)
total = balance + deposit

#12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
temperature = int(36.7)
degree = int(28.4)
climate = temperature + degree

#13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
climate = temperature / degree

#14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
climate = temperature * degree

#15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
climate = temperature // degree

#16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
climate = temperature % degree


print("Balance: " + str(total)) #11 задание
print(temperature + degree) #12 задание
print(temperature / degree) #13 задание
print(temperature * degree) #14 задание
print(temperature // degree) #15 задание
print(temperature % degree) #16 задание