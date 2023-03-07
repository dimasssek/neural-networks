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
