# Завдання 5
# Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.

width, height = int(input('Введiть ширину прямокутника: ')), int(input('Введiть висоту прямокутника: '))
for i in range(height):
    for y in range(width):
        print('*', end='')
    print()