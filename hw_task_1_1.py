import random
import pandas as pd

res = []
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

print(data.head())
for el in lst:
    if el == 'robot':
        res.append('1')
    else:
        res.append('0')

print('robot = 1, human = 0')
for idx, num in enumerate(res[:5], start=0):
    print(f"{idx}. {num}")
