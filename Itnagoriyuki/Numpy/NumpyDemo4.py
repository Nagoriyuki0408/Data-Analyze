
# coding=utf-8
import numpy as np

# 定义美国youtube视频数据文件路径
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
# 定义英国youtube视频数据文件路径
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# 使用loadtxt读取美国youtube视频数据，delimiter指定分隔符为逗号，dtype指定数据类型为整数
# unpack=True会将数据进行转置，这里注释掉了，所以不转置
# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")

# 打印t1，这里注释掉了
# print(t1)
# 打印t2，t2是读取的美国youtube视频数据
print(t2)

print("*"*100)

# 取行
# 打印t2的第3行（索引为2）
# print(t2[2])

# 取连续的多行
# 打印t2的第3行到最后一行（索引为2到结尾）
# print(t2[2:])

# 取不连续的多行
# 打印t2的第3行、第9行和第11行（索引为2, 8, 10）
# print(t2[[2,8,10]])

# 打印t2的第2行（索引为1）的所有列
# print(t2[1,:])
# 打印t2的第3行到最后一行（索引为2到结尾）的所有列
# print(t2[2:,:])
# 打印t2的第3行、第11行和第4行（索引为2, 10, 3）的所有列
# print(t2[[2,10,3],:])

# 取列
# 打印t2的第一列（索引为0）的所有行
# print(t2[:,0])

# 取连续的多列
# 打印t2的第3列到最后一列（索引为2到结尾）的所有行
# print(t2[:,2:])

# 取不连续的多列
# 打印t2的第一列和第三列（索引为0, 2）的所有行
# print(t2[:,[0,2]])

# 去行和列，取第3行，第四列的值
# a = t2[2,3]
# print(a)
# print(type(a))

# 取多行和多列，取第3行到第五行，第2列到第4列的结果
# 去的是行和列交叉点的位置
b = t2[2:5,1:4]
# print(b)

# 取多个不相邻的点
# 选出来的结果是（0，0） （2，1） （2，3）
c = t2[[0,2,2],[0,1,3]]
print(c)