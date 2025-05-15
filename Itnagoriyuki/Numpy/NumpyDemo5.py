# coding for
import numpy as np
import matplotlib.pyplot as plt

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
# 使用 numpy 加载美国 youtube 视频数据，数据类型为 int
t_us = np.loadtxt(us_file_path, delimiter=",", dtype="int")

# 从加载的数据中提取评论数（最后一列）
t_us_comments = t_us[:, -1]

# 过滤评论数，只保留小于等于 5000 的数据，去除异常值
t_us_comments = t_us_comments[t_us_comments <= 5000]

# 打印过滤后的评论数的最大值和最小值
print(t_us_comments.max(), t_us_comments.min())

# 定义组距为 250
d = 250

# 计算组数，用最大值减去最小值，然后除以组距
bin_nums = (t_us_comments.max() - t_us_comments.min()) // d

# 创建一个图形，设置大小和分辨率
plt.figure(figsize=(20, 8), dpi=80)

# 绘制直方图，使用过滤后的评论数数据和计算出的组数
plt.hist(t_us_comments, bin_nums)

# 显示图形
plt.show()