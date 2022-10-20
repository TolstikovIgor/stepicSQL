
'''7.1 Цикл for
Python is awesome
Напишите программу, которая выводит слова «Python is awesome!» (без кавычек) 10 раз.'''
for i in range(10):
    print('Python is awesome!')
    
'''Повторяй за мной 1
Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное 
количество раз.'''
s = input()
n = int(input())

for i in range(n):
    print(s)
    
'''Последовательность символов
Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:'''
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

'''Звездный прямоугольник
На вход программе подается натуральное число nn.
Напишите программу, которая печатает звездный прямоугольник размерами n \times 19n×19.'''
n = int(input())

for i in range(n):
    print('*' * 19)
    
'''Повторяй за мной 2
Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9, каждая с указанной 
строкой текста.'''
n = input()
for i in range(10):
    print(i, n)
    
'''Квадрат числа
На вход программе подается натуральное число nn. Напишите программу, которая для каждого из чисел от 00 до nn (включительно)
 выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).'''
n = int(input())

for i in range(n+1):
    print('Квадрат числа', i, 'равен', i * i)
    
'''Звездный треугольник
На вход программе подается натуральное число n \, (n \ge 2)n(n≥2) – катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звездный треугольник в соответствии с примером.'''
n = int(input())

for i in range(n):
    print('*' * (n - i))
    
'''Популяция
На вход программе подается три натуральных числа m, \, p, \, nm,p,n:
m:m: стартовое количество организмов;
p:p: среднесуточное увеличение в %;
n:n: количество дней для размножения.
Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, 
начиная с 11 и заканчивая nn-м днем.'''
m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)
    
    
'''7.2 Цикл for: функция range
Последовательность чисел 1
Даны два целых числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно.'''
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)
    
'''Последовательность чисел 2 🌶️
Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания, если 
m < nm<n, или в порядке убывания в противном случае.'''
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
        
'''Последовательность чисел 3 🌶️
Даны два целых числа mm и nn (m > nm>n). Напишите программу, которая выводит все нечетные числа от mm до nn включительно в 
порядке убывания.'''
m, n = int(input()), int(input())
if m % 2 == 1:
    for i in range(m, n - 1, -2):
        print(i)
else:
    for i in range(m - 1, n - 1, -2):
        print(i)

===
m, n = int(input()), int(input())
for i in range(m - 1 + m % 2, n - 1, -2):
    print(i)      
      
'''Последовательность чисел 4
Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно 
удовлетворяющие хотя бы одному из условий:

число кратно 17;
число оканчивается на 9;
число кратно 3 и 5 одновременно.'''
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):
        print(i)
        
'''Таблица умножения
Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.'''
n = int(input())
for i in range(10):
    print(n, 'x', i + 1, '=', n * (i + 1))
    
    
'''7.3 Частые сценарии
Количество чисел
На вход программе подаются два целых числа aa и bb (a \le b)(a≤b). Напишите программу, которая подсчитывает количество чисел
 в диапазоне от aa до bb включительно, куб которых оканчивается на 44 или 99.'''
a, b = int(input()), int(input())
counter = 0
for i in range(a, b+1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter = counter + 1
print(counter)

'''Сумма чисел
На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, 
которая подсчитывает сумму введенных чисел. '''
n = int(input())
total = 0
for i in range(n):
    a = int(input())
    total = total + a
print(total)

'''Асимптотическое приближение
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения'''
from math import *

n = int(input())
num = 0
for i in range(1, n+1):
    num = num + (1 / i)
    num2 = num - log(n)
print(num2)

'''Сумма чисел 2
На вход программе подается натуральное число nn. Напишите программу, которая подсчитывает сумму тех чисел от 11 до nn
 (включительно) квадрат которых оканчивается на 2, \, 52,5 или 88.'''
n = int(input())
counter = 0
for i in range(1, n+1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 == 8:
        counter = counter + i
print(counter)

'''Факториал
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет n!n!.'''
import math

n = int(input())
total = 1
for i in range(1, n):
    total = math.factorial(n)
    
print(total)

'''Без нулей
Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.'''
total = 1
for i in range(10):
    a = int(input())
    if a != 0:
        total = total * a
print(total)

'''Сумма делителей
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет сумму всех его делителей.'''
n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total = total + i
print(total)

'''Знакочередующаяся сумма
На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы 
1-2+3-4+5-6 + \ldots + (-1)^{n+1}n.
1−2+3−4+5−6+…+(−1) 
n+1'''
n = int(input())
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total = total - i
    else:
        total = total + i
print(total)

'''Наибольшие числа 🌶️🌶️
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. Напишите 
программу, которая выводит наибольшее и второе наибольшее число последовательности.'''
n = int(input())
max1 = 0
max2 = 1
for i in range(1, n+1):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
print(max1, max2, sep='\n')

'''Only even numbers 🌶️
Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.'''
count = 0
for i in range(1, 11):
    n = int(input())
    if n % 2 == 0:
        count += 1
if count == 10:
    print('YES')
else:
    print('NO')
    
'''Последовательность Фибоначчи 🌶️
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.'''
n = int(input())
a = 0
b = 1
for i in range(0, n):
    a, b = b, a + b
    print(a, end=' ')
    
    
'''7.4 Цикл while
До КОНЦА 1
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово
 «КОНЕЦ» (без кавычек). Напишите программу, которая выводит члены данной последовательности.'''
text = input()
while text != 'КОНЕЦ':
    print(text)
    text = input()
    
'''До КОНЦА 2
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово 
«КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). Напишите программу, которая выводит члены данной 
последовательности.'''
a = input()
while a != 'КОНЕЦ' and a != 'конец':
    print(a)
    a = input()
    
'''Количество членов
На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно
 из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Напишите программу, которая выводит общее 
 количество членов данной последовательности.'''
a = input()
n = 0
while a not in ('стоп', 'хватит', 'достаточно'):
    a = input()
    n = n + 1
print(n)

'''Пока делимся
На вход программе подается последовательность целых чисел делящихся на 77, каждое число на отдельной строке. Концом 
последовательности является любое число не делящееся на 77. Напишите программу, которая выводит члены данной последовательности.'''
a = int(input())
while a % 7 == 0:
    print(a)
    a = int(input())
    
'''Сумма чисел
На вход программе подается последовательность целых чисел, каждое число на отдельной строке. Концом последовательности является любое отрицательное число. Напишите программу, которая выводит сумму всех членов данной последовательности.'''
n = int(input())
a = 0
while n >= 0:
    a = a + n
    n = int(input())
print(a)  

'''Количество пятерок
На вход программе подается последовательность целых чисел от 11 до 55, характеризующее оценку ученика, каждое число на отдельной 
строке. Концом последовательности является любое отрицательное число, либо число большее 55. Напишите программу, которая выводит
 количество пятерок.'''
a = int(input())
n = 0
while 0 < a < 6:
    if a == 5:
        n = n + 1
    a = int(input())
print(n)

'''Ведьмаку заплатите чеканной монетой
Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево, к тому же ведьмак не принимает
купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1, \, 5, \, 10, \, 251,5,10,25.
Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.'''
n = int(input())
count = 0
while n >= 25:
    count += 1
    n = n - 25
while 10 <= n < 25:
    count += 1
    n = n - 10
while 5 <= n < 10:
    count += 1
    n = n - 5
while 1 <= n < 5:
    count += 1
    n = n -1
print(count)


'''7.5 Цикл while: обработка цифр числа
Обратный порядок 1
Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.'''
n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    n = n // 10  # удалить последнюю цифру из числа
    print(last_digit)
    
'''Обратный порядок 2
Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.'''
n = int(input())
while n:
    print(n % 10, end='')
    n //= 10
    
'''max и min
Дано натуральное число n, \, (n \ge 10)n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.'''
n = input()
mx = max(n)
mn = min(n)

print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)

'''Все вместе
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.'''
n = int(input())
summ = 0
counter = len(str(n))
compos = 1
argv = 0
first_d = n // (10 ** (counter - 1))
last_d = n % 10
sum_f_l = first_d + last_d
while n != 0:
    summ = summ + n % 10
    compos = compos * (n % 10)
    argv = summ / counter
    n = n // 10
print(summ)
print(counter)
print(compos)
print(argv)
print(first_d)
print(sum_f_l)

'''Вторая цифра
Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.'''
n = int(input())
second_d = 0
while n > 9:
    second_d = n % 10
    n = n // 10    

print(second_d)

'''Одинаковые цифры
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.'''
n = int(input())
flag = True

while n > 9:
    last_d = n % 10
    n = n // 10
    sec_d = n % 10
    if last_d != sec_d:
        flag = False
if flag:
    print('YES')
else:                
    print('NO') 
    
'''Упорядоченные цифры 🌶️
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.'''
n = int(input())
flag = True

while n > 9:
    last_d = n % 10
    n = n // 10
    sec_d = n % 10
    if last_d > sec_d:
        flag = False
if flag:
    print('YES')
else:                
    print('NO')
    

'''7.6 break, continue и else
Что покажет приведенный ниже фрагмент кода?'''
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
# 0*1*2*3*4*5*6*7*
        
i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20
# 100*80*60*

n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')
# 9*8*7*6*5*4*3*1*0*
    
result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
print(result)
# 25

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)
# 25

'''Наименьший делитель
На вход программе подается число n > 1. Напишите программу, которая выводит его наименьший отличный от 11 делитель.'''
n = int(input())
a = 2
while n != 0:
    if n % a == 0:
        break
    else:
        a = a + 1
print(a)

'''На вход программе подается натуральное число nn. Напишите программу, которая выводит числа от 11 до nn включительно за исключением:

чисел от 55 до 99 включительно;
чисел от 1717 до 3737 включительно;
чисел от 7878 до 8787 включительно.'''
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
    
'''Будет ли выполнен блок кода else, в приведенном ниже фрагменте кода?'''
n = 0
while n < 10:
    n += 2
    print(n)
else:
    print('Цикл завершен.')
# Да
    
n = 0
while n < 10:
    n += 2
    if n == 8:
        break
    print(n)
else:
    print('Цикл завершен.')
# Нет
    
n = 0
while n < 10:
    n += 2
    if n == 7:
        break
    print(n)
else:
    print('Цикл завершен.')
# Да


'''7.7 Поиск ошибок и ревью кода
Ревью кода-1 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают
 10^6. Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
  Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.'''
count = 0
p = 1  # 1
for i in range(1, 11):  # 2
    x = int(input())
    if x >= 0:  # 3
        p = p * x
        count = count + 1
if count > 0:
    print(count)  # 4
    print(p)
else:
    print('NO')
    
'''Ревью кода-2 🌶️🌶️
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают
 10^6. Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное 
 отрицательное число в последовательности. Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился
  и написал программу неправильно.'''
mx = -1_000_000  # 1
s = 0
for i in range(10):  # 2
    x = int(input())
    if x < 0:
        s = s + x  # 3
        if x > mx:  # 4
            mx = x
if s < 0:  # 5
    print(s)
    print(mx)
else:
    print('NO')
    
'''Ревью кода-3
На обработку поступает последовательность из 7 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10^6.
Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности или 00, если чётных чисел в последовательности нет. Программист торопился и написал программу неправильно.'''
s = 0  # 1
for i in range(7): # 2
    n = int(input())  # 3
    if n % 2 == 0:  # 4
        s = s + n
print(s)
    
'''Ревью кода-4 🌶️🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран максимальную цифру числа, кратную 3.
 Если в числе нет цифр, кратных 3, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.'''
n = int(input())
max_digit = -1  # 1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:  # 2
            max_digit = digit  # 3
    n = n // 10  # 4
if max_digit < 0:  # 5
    print('NO')
else:
    print(max_digit)

'''Ревью кода-5 🌶️
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран его первую (старшую) цифру. 
Программист торопился и написал программу неправильно.'''
n = int(input())
while n > 9:  # 1
    n = n // 10  # 2
print(n)

'''Ревью кода-6
На обработку поступает натуральное число. Нужно написать программу, которая выводит на экран произведение цифр введенного числа. 
Программист торопился и написал программу неправильно.'''
n = int(input())  # 1
product = 1  # 2
while n > 0:  # 3
    digit = n % 10
    product = product * digit
    n //= 10
print(product)


'''7.8 Вложенные циклы Часть 1
Таблица-1
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу размером n \times 3n×3 состоящую из 
данного числа (числа отделены одним пробелом).'''
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
    
'''Таблица-2
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу размером n \times 5n×5, где в 
i-ой строке указано число ii (числа отделены одним пробелом).'''
n = int(input())
for i in range(1, n+1):
    for j in range(5):
        print(i, end=' ')
    print()
    
'''Таблица-3
Дано натуральное число n \, (n \le 9)n (n≤ 9). Напишите программу, которая печатает таблицу сложения для всех чисел от 11 до 
n в соответствии с примером.'''
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        s = i + j
        print(i, '+', j, '=', s)
    print()
    
'''Звездный треугольник 🌶️🌶️
Дано нечетное натуральное число nn. Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным 
n в соответствии с примером:'''
n = int(input())
for i in range(n // 2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for k in range(n // 2, 0, -1):
    for l in range(k):
        print('*', end='')    
    print()
    
'''Численный треугольник 1
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник в соответствии с примером:'''
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()

'''12 месяцев
Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.'''
for n in range(1, 365):
    for k in range(1, 365):
        for m in range(1, 365):
            if n * 28 + k * 30 + m * 31 == 365:
                print('n=', n, 'k=', k, 'm=', m)

'''Старинная задача
Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 1010 рублей, за корову
– 55 рублей, за теленка – 0.50.5 рубля и надо купить 100100 голов скота?'''
for b in range(1, 100):
    for k in range(1, 100):
        for t in range(1, 100):
            if b * 10 + k * 5 + t * 0.5 == 100:
                print('b=', b, 'k=', k, 't=', t)
                
'''Гипотеза Эйлера о сумме степеней 🌶️🌶️
В 1769 году Леонард Эйлер сформулировал обобщенную версию Великой теоремы Ферма, предполагая, что по крайней мере nn энных степеней
 необходимо для получения суммы, которая сама является энной степенью для n > 2n>2. Напишите программу для опровержения гипотезы 
 Эйлера (продержавшейся до 1967 года), и найдите четыре положительных целых числа, сумма 5-х степеней которых равна 5-й степени 
 другого положительного целого числа.'''
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** (1 / 5))
                if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
                    print(a + b + c + d + e)
                    

'''7.9 Вложенные циклы. Часть 2
Численный треугольник 3
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:'''
a = 0
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        a = a + 1
        print(a, end=' ')
    print()
    
'''Численный треугольник 4
Дано натуральное число nn. Напишите программу, которая печатает численный треугольник с высотой равной nn, в соответствии с примером:'''
n = int(input())
for i in range(0, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
    
'''Делители-1 🌶️
На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит натуральное число из 
отрезка [a; \, b][a;b] с максимальной суммой делителей.'''
a, b = int(input()), int(input())
count = 0
max_s = 0
for i in range(a, b + 1):
    sum_d = 0
    for j in range(1, i + 1):
        if i % j == 0:
            sum_d = sum_d + j
            if sum_d >= max_s:
                max_s = sum_d
                count = i
print(count, max_s, sep=' ')

'''Делители-2
На вход программе подается натуральное число nn. Напишите программу, выводящую графическое изображение делимости чисел от 11
 до nn включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.'''
n = int(input())
for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count = count + 1
    print(i, '+' * count, sep='')
    
'''Цифровой корень
На вход программе подается натуральное число nn. Напишите программу, которая находит цифровой корень данного числа. Цифровой
 корень числа nn получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить 
 этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.'''
n = int(input())
while n > 9:
    digit = 0
    while n > 0:
        last = n % 10
        digit = digit + last
        n = n // 10
    n = digit
print(n)

'''Сумма факториалов
Дано натуральное число nn. Напишите программу, которая выводит значение суммы 1!+2!+3!+\ldots+n!1!+2!+3!+…+n!.'''
from math import factorial

n = int(input())
num = 0
for i in range(1, n+1):
    num = num + factorial(i)
print(num)

'''Простые числа
На вход программе подается два натуральных числа aa и bb (a < ba< b). Напишите программу, которая находит все простые числа 
от aa до bb включительно.'''
a = int(input())
b = int(input())
for x in range(a, b + 1):
    counter = 0
    for i in range(1, x + 1):
        if x % i == 0:
            counter += 1
    if counter == 2:
        print(x)
        