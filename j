s = input().split('.')[0].replace(' ', '').upper()
max_char = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
for char in s:
   max_char[char]+=1
m = max(max_char, key=lambda k: max_char[k])
print(m, max_char[m])


np.random.seed(242) 
s = pd.Series(data=np.random.normal(size=200)) 
s = s.map(lambda x: x ** 2) 
s.index *= 2 
print(s.values[1::2][(s.values[1::2] < 2.5)].sum()) 
print(len(s.values[s.values < 0]))

Дан текст на языке племени Мумба-Юмба. Выведите все слова,
встречающиеся в тексте, разделяя их пробелом. Слова должны быть
отсортированы по убыванию их количества появления в тексте, а при 
одинаковой частоте появления — в алфавитном порядке.
Замечание. a)[(2, 'hi'), (1, 'what'), (3, 'is')] . Cтандартная сортировка будет
сортировать список кортежей, при этом кортежи сравниваются по первому
элементу, а если они равны — то по второму.
b) параметр key в сортировке.

n = int(input())
radii = set(map(int, input().split()))

# Определяем количество снеговиков, которое можно слепить
k = len(radii) // 3

# Составляем кортежи снеговиков
snowmen = []
for i in range(k):
    big, middle, small = sorted((radii.pop() for _ in range(3)), reverse=True)
    snowmen.append((big, middle, small))

# Выводим результат
print(k)
for snowman in snowmen:
    print(*snowman)

n = int(input())
radii = list(map(int, input().split()))

# создаем словарь с количеством комов каждого радиуса
count = {}
for r in radii:
    if r not in count:
        count[r] = 1
    else:
        count[r] += 1

# сортируем радиусы в порядке возрастания
sorted_radii = sorted(count.keys())

# перебираем все комбинации радиусов
max_snowmen = 0
best_snowmen = []
for i in range(len(sorted_radii)):
    for j in range(i+1, len(sorted_radii)):
        for k in range(j+1, len(sorted_radii)):
            r1, r2, r3 = sorted_radii[i], sorted_radii[j], sorted_radii[k]
            if r1 != r2 and r2 != r3 and count[r1] > 0 and count[r2] > 0 and count[r3] > 0:
                count[r1] -= 1
                count[r2] -= 1
                count[r3] -= 1
                max_snowmen += 1
                best_snowmen.append((r3, r2, r1))

print(max_snowmen)
for s in best_snowmen:
    print(s[0], s[1], s[2])
