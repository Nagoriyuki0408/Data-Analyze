import matplotlib.pyplot as plt
from matplotlib import font_manager

# 数据准备
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)

# 字体设置
my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\Deng.ttf")

# 创建图形
plt.figure(figsize=(10, 5), dpi=80)

# 绘制折线图
plt.plot(x, a, label="我自己", marker='o')  # 自己的数据
plt.plot(x, b, label="我同桌", marker='s')  # 同桌的数据

# 设置x轴刻度和标签
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(list(x), _xtick_labels, rotation=45, fontproperties=my_font)

# 设置y轴刻度
plt.yticks(range(0, 9))

# 添加网格
plt.grid(alpha=0.4)

# 添加描述性信息
plt.xlabel("岁数/岁", fontproperties=my_font)
plt.ylabel("个数/个", fontproperties=my_font)
plt.title("不同岁数的男女朋友数量对比", fontproperties=my_font)

# 添加图例
plt.legend(prop=my_font)

# 保存并显示图表
plt.savefig("./friends_comparison.svg")
plt.show()