'''
图片大小和像素直接关系的内容能否正确显示，谨慎使用
plt.figure(figsize=(16,8),dpi=600) 
'''


import matplotlib.pyplot as plt  
  
# 设置字体为“微软雅黑”（确保你的系统中已安装此字体） 
#plt.figure(figsize=(16,8),dpi=600) 
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 这一步指定默认字体为微软雅黑  
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题  
  
# 现在绘制图形并添加中文标签  
plt.plot(['天', '地', '人'],[1, 2, 3])
plt.title('这是一个中文标题')  
plt.xlabel('x轴')  
plt.ylabel('y轴')  
  
plt.show()