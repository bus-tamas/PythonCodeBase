import pandas as pd
import seaborn as sb
import numpy as np

s = pd.Series([4.5, 7, 1.3, 9.31],index=['a','b','c','d'])
print(s)

s['a':'c']
print(s)

s1 = pd.Series([1 , 2 , 3],index=['a','b','c'])
s2 = pd.Series([2 , 5 , 9],index=['d','a','b'])

print(s1+s2)

print(s1.add(s2,fill_value=0))

s1.multiply(s2,fill_value=0)