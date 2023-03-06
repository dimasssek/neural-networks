s = input().split('.')[0].replace(' ', '').upper()
max_char = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
for char in s:
   max_char[char]+=1
m = max(max_char, key=lambda k: max_char[k])
print(m, max_char[m])
