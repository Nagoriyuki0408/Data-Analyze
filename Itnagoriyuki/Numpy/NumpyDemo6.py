# coding for
import numpy as np
import matplotlib.pyplot as plt

# 定义美国视频数据文件的路径
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
# 定义英国视频数据文件的路径
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"

# 使用 numpy 的 loadtxt 函数加载英国视频数据，指定分隔符为逗号，数据类型为整数
# t_uk 是一个 numpy 数组，每一行代表一个视频的数据
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 过滤数据：只保留点赞数小于等于 500000 的视频数据
# t_uk[:, 1] 表示 t_uk 数组的所有行的第二列（点赞数）
# t_uk[t_uk[:, 1] <= 500000] 表示选取 t_uk 数组中第二列小于等于 500000 的所有行
t_uk = t_uk[t_uk[:, 1] <= 500000]

# 从过滤后的数据中提取评论数和点赞数
# t_uk[:, -1] 表示 t_uk 数组的所有行的最后一列（评论数）
t_uk_comments = t_uk[:, -1]
# t_uk[:, 1] 表示 t_uk 数组的所有行的第二列（点赞数）
t_uk_like = t_uk[:, 1]

# 创建一个图形，并设置大小和分辨率
plt.figure(figsize=(20, 8), dpi=80)

# 创建散点图，x 轴为点赞数，y 轴为评论数
plt.scatter(t_uk_like, t_uk_comments)

# 显示图形
plt.show()