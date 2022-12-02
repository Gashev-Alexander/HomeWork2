import os

os.system('cls')
import random

massiv = ['First', 'Second ', 'Cooking ', 'Auto ', 'Guns', 'Третий']
random.shuffle(massiv)
print(f'test #1 {massiv}')
random.shuffle(massiv)
print(f'test #2 {massiv}')
random.shuffle(massiv)
print(f'test #3 {massiv}')