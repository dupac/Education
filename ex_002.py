'''
phrase = input()
print(phrase)
'''

'''
phrase = input("Введите строку: ")
print(phrase)
'''

'''
name = "Пользователь"
print("Добрый день,", name, ".")

'''

'''
name = "Пользователь"
print("Добрый день, ", name, ".", sep="")
'''

'''
name = "Пользователь"
print(f"Добрый день, {name}.")
'''

'''
print(f"{123:0>9}")
print(f"{123:-<9}")
print(f"{123: ^9}")
'''

'''
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
'Results of the 2016 Referendum'
'''

"""
- `\n` — переход на новую строку;
- `\t` — табуляция;
- `\r` — возврат каретки в начало строки;
- `\b` — возврат каретки на один символ.

print("\n\t\b\r111\111111\7221")
"""

'''
print("Привет, Пользователь!")
print("Как дела?")
'''
'''
print("Сложно" + "подчинённый")
'''

'''
print("-" * 10)
'''

'''
#Первый результат — результат сложения (конкатенации) двух строк. 
#Второй — результат сложения целых чисел, которые были преобразованы из строк функцией `int()`.
n_1 = "1"
n_2 = "2"
print(n_1 + n_2)
n_1 = int(n_1)
n_2 = int(n_2)
print(n_1 + n_2)
'''

'''
x = 3.89
x = int(x)
print(x)
'''


'''
width = "3.7"
height = "2.5"
s = float(width) * float(height)
print(s)
'''

'''
int_number = int(input())
float_number = float(input())
'''

'''
n = 25
x = 0.5

print(n + x)
print(n - x)
print(n * x)
print(n / x)
print(n ** x)
'''

'''
- сложение — `x + y`;
- вычитание — `x - y`;
- умножение — `x * y`;
- деление — `x / y`;
- возведение в степень `x ** y`.
'''

'''
print(90 / 2)
'''

'''
# корень из четырех
print(f"{4 ** 0.5:.3f}")
'''

'''
- целочисленное деление — `x // y`;
- остаток от деления — `x % y`.
'''
'''
print(5/2)
print(5//2)
print(5%2)
'''

'''
last_digit = 123 // 10
last_digit2 = last_digit % 10
print("!1! -", last_digit)
print("!2! -", last_digit2)

last_digit3 = 123 // 10 % 10
print("!3! -", last_digit3)


penultimate_digit = 123 // 10 % 10
print("!4! -", penultimate_digit)
'''









