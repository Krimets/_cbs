# Завдання 5
# З клавіатури вводиться рядок, в якому є інформація про прізвище, ім'я, дату народження, електронну адресу та відгук
# про курси учня. Написати функцію, яка, використовуючи регулярні вирази, витягне дані з рядка і поверне словник.

import re

# a = 'IvanovIvan01-12-2000test123@gmail.comВідгукпрокурсиучня'
a = input('З клавіатури вводиться рядок:\n>>> ')
b = ['прізвище', 'ім\'я', 'дата народження', 'email', 'відгук']
d = {}
c = 0

result = re.findall(r'(^[A-ZА-ЯІЇЄҐ][a-zа-яіїєґ ]+)([A-ZА-ЯІЇЄҐ][a-zа-яіїєґ ]+)([\d\- ]+)(\w+@\w+\.com)(.*)', a)
for i in b:
    d[i] = result[0][c]
    c += 1
for key, value in d.items():
    print(f"{key}: {value}")
