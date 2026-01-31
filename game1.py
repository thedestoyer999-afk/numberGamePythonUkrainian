import random

print('''Ласкаво просимо до гри 1!
Я загадую число від 1 до 100 а ви маєте його відгадати
якщо ви вгадали число, то ви виграли, якщо ні - програли
Удачі!''')
difficulty = input('''Вибери складність:
1 - легка (10 спроб)
2 - середня (7 спроб)
3 - важка (5 спроб)
''')
if difficulty == '1':
    attempts = 10
    defficulty_uk = 'легку'
elif difficulty == '2':
    attempts = 7
    defficulty_uk = 'середню'
elif difficulty == '3':
    attempts = 5
    defficulty_uk = 'важку'

print(f'Ви вибрали {defficulty_uk} складність')
number_to_guess = random.randint(1, 100)

entered_number = int(input ('Введіть число (від 1 до 100): '))

if entered_number != number_to_guess:
    for attempt in range(attempts - 1):
        if entered_number < number_to_guess:
            print (f'{entered_number} менше за загадане число')
            entered_number = int(input ('Спробуйте ще раз: '))
        elif entered_number > number_to_guess:
            print (f'{entered_number} більше за загадане число')
            entered_number = int(input ('Спробуйте ще раз: '))
        elif entered_number == number_to_guess:
            print ('Ви вгадали число! Ви виграли!')
            break
    print (f'Ви програли! Загадане число було {number_to_guess}')