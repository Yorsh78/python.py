# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

x = abs(int(input('Первая циферка - ')))
y = abs(int(input('Вторая циферка - ')))
S = x + y
P = x * y
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)