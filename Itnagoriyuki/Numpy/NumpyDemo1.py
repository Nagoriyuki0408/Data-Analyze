# 导入numpy库，用于后续创建和操作数组
import numpy as np

# 创建一个numpy数组t1，包含1到5的整数
t1 = np.array([1, 2, 3, 4, 5])

# 输出数组t1的内容
print(t1)
# 输出数组t1的数据类型
print(type(t1))

# 创建一个numpy数组t2，包含0到9的整数
t2 = np.array(range(10))
print(t2)

# 使用arange函数创建一个numpy数组t3，包含0到9的整数
t3 = np.arange(10)
print(t3)

# 使用arange函数创建一个numpy数组t4，包含1到9的奇数
t4 = np.arange(1, 10, 2)
print(t4)
# 输出数组t4的数据类型
print(t4.dtype)

# 使用arange函数创建一个numpy数组t5，包含1到9的奇数，数据类型指定为float32
t5 = np.arange(1, 10, 2, dtype=np.float32)
print(t5)
print(t5.dtype)

t7 = t4.astype("int8")
print(t7)
print(t7.dtype)

t8 = np.round(t5, 2)
print(t8)
print(t8.dtype)