a = 11
a += 2
print(a)

a = 11
a -= 2
print(a)

a = 11
a *= 2
print(a)

a = 11
a /= 2
print(a)

#целочисленное деление
a = 11
a //= 2
print(a)

#остаток от деления
a = 11
a %= 2
print(a)

#возведение в степень
a = 11
a **= 2
print(a)

"""
 \n перенос на новую строку
 \t табуляция
 \ экранирование
 + конкатенация
 * 3 дублирование
"""


#длина строки
a = "asdasdasd"
print(len(a))

#доступ по индексу
a = "Длинная строка"
print('первый символ равен "' + a[0] + '"\nпятый символ равен "' + a[4] + '"\nпредпоследний символ равен "' + a[-2] + '"')

#срезы
a = "просто_строка"
print(a[1:2] + '\n' + a[6:] + '\n' + a[2:-2] + '\n' + a[:] + '\n' + a[:10:2] + '\n' + a[::-1])


a = 'привет'
b = 'пока'
print('сначала он сказал %s ' % a)

print('сначала он сказал %s, а потом добавил %s' % (b, a))

print('сначала он сказал {}, а потом добавил {}'.format(a, b))

print('сначала он сказал {1}, а потом добавил {0}'.format(a, b))

print(f'сначала он сказал {a}, а потом добавил {b}')