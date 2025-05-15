
# 导入绘图库和字体管理器
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 加载自定义字体文件
my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\Deng.ttf")

# 准备电影名称和对应的票房数据
a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]
b = [56.02, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88, 6.86, 6.58, 6.23]

# 创建一个新的图形对象，并设置图形的大小和分辨率
plt.figure(figsize=(20,15),dpi=80)

# 绘制柱状图，x轴为电影索引，y轴为票房数据
plt.bar(range(len(a)),b)

# 设置x轴标签，使用自定义字体并旋转90度以适应长文本
plt.xticks(range(len(a)),a,fontproperties=my_font,rotation=90)

# 保存图形到文件
plt.savefig("./test1.png")

# 显示图形
plt.show()