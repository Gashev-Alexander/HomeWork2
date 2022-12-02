import os
os.system('cls')

with open('file.txt','r') as f:
    a = f.read().split('\n')
print(a)

elements = []
n = int(input('Введите число N: '))

for i in range (-n,n+1):
    elements.append((i))
print(elements)

res = 1
for item in a:
    res *= elements[int(item)]

print(res)