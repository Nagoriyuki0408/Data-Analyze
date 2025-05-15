import pandas as pd

# 从列表创建 Series
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
# 输出:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# 从字典创建 Series (键变为索引)
data = {'a': 10, 'b': 20, 'c': 30}
s = pd.Series(data)
print(s)
# 输出:
# a    10
# b    20
# c    30
# dtype: int64

# 指定索引
s = pd.Series(data, index=['b', 'c', 'd'])
print(s)
# 输出:
# b    20.0
# c    30.0
# d     NaN
# dtype: float64