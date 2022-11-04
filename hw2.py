'''
Синтаксична помилка:
a = 3
if a = 3:
    print('а дорівнює 3')
    
Буде помилка, оскільки оператор присвоювання "=" поплутано з оператором порівняння "=="

Логічна помилка:
weeks = 5
days = 3
total_days = days*7 + weeks

Правильно:
total_days = days + weeks*7


1 / 0
буде ZeroDivisionError - помилка ділення на нуль

0 / 1
0.0 - арифметичний результат, виводится у форматі float

Коментарі необхідні, щоб самому не заплутатися у коді, а також, щоб інші програмісти розуміли логіку коду.

Змінна це вказівник на якесь значення, яке зберігається у пам'яті.

'''

a = int(float(input('Enter one number: ')))
b = int(float(input('Enter another number: ')))

print('Your numbers:', a, b)

print(a*b)
print(a-b)
print(a+b)
print(a/b)
print(a%b)
print(a//b)
print(a, 'в степені', b, 'це', a**b)

name = input('Enter your name: ')
sname = input('Enter your second name: ')
age = input('Enter your age: ')

print(name, ' ', sname, '\n', 'You are ', age, ' years old.', sep = '')