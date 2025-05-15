a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b =[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x=range(1,32)
x_2=range(40,71)

# 加载本地字体文件，用于支持中文显示
my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\Deng.ttf")

# 创建一个新的图像对象，指定图像大小和分辨率
plt.figure(figsize=(20,8),dpi=80)

# 绘制散点图，红色标记数据序列a
plt.scatter(x,a,s=50,c='r',marker='o',label='point')
# 绘制散点图，蓝色标记数据序列b
plt.scatter(x_2,b,s=50,c='b',marker='o',label='point')

_x=list(x)+list(x_2)
# 生成x轴标签，表示月份
_xtick_labels = ["10月{}日".format(i) for i in _x]

# 设置x轴标签，旋转45度，使用自定义字体
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)

plt.yticks(a)

plt.legend(loc="upper left",prop=my_font)

plt.xlabel("十月/日",fontproperties=my_font)
plt.ylabel("温度/摄氏度",fontproperties=my_font)
plt.title("温度变化",fontproperties=my_font)

# 保存图像为SVG格式文件
plt.savefig('points.svg')

# 显示图像
plt.show()