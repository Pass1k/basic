print('Задача 5. Часы')

# Напишите программу,
# которая получает на вход число n — количество минут, — затем считает,
# сколько это будет в часах и сколько минут останется,
# и выводит на экран эти два результата.
minute = int(input('Введите количество минут: '))
hours = minute // 60
minutes = minute % 60
print(f'У вас осталось {hours} часов и {minutes} минут')