# Программа принимает на вход три символа через пробел в одну строку.
# Необходимо вывести код каждого символа при помощи функции ord в определенном формате.

# a, b, c = input().split()
# print('Simvol code %s is %s.' %(a, ord(a)), 'Simvol code %s , is %s.' %(b, ord(b)),
# 'Simvol code %s is %s.' %(c, ord(c)), sep='\n')
# -------------------------------------

# На вход подается строка.
# Ваша задача отформатировать строку так,
# чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.

# a = input().lower()
# b = a[0:3].upper()
# c = a[-3:].upper()
# print(b + a[3:-3] + c)

# или

# a = input().lower()
# print(a[0:3].upper() + a[3:-3] + a[-3:].upper())
# -------------------------------------

# Напишите программу, которая проверяет начинается ли введенная фраза строкой mam вне зависимости от регистра букв

# print(input().lower().startswith('mam'))
# -------------------------------------

# Ваша задача закодировать оттенки цветов согласно RGB модели.

# r, g, b = str(hex(int(input()))).strip('0x'), str(hex(int(input()))).strip('0x'), str(hex(int(input()))).strip('0x')
# r = r.zfill(2).upper()
# g = g.zfill(2).upper()
# b = b.zfill(2).upper()
# print('#' + r + g + b)
# -------------------------------------

# Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом,
# чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы

# a, b = map(str, input().split())
# list1 = list(a)
# list2 = list(b)
# print('-'.join(list1).upper(), '-'.join(list2).upper())
# -------------------------------------

