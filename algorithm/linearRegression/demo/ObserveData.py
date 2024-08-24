# import package
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from matplotlib.font_manager  import FontProperties

# import data
df=pd.read_csv('./new_train.csv',encoding='utf-8')
# print(df.head())
# 计算相关关系
corrmat=df.corr().sort_values(by='房价').iloc[-10:-1]
#print(corrmat['房价'].index)


#绘制相关关系图

#plt.figure(figsize=(16,8),dpi=600) #设置图片大小
plt.rcParams['axes.unicode_minus']=False #解决图像中负号显示为方框的问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] #
plt.xticks(rotation=45)
plt.title("特征-房价(相关系数)")
plt.ylabel('相关系数')
plt.xlabel('相关性最强的10个特征')
plt.scatter(corrmat['房价'].index ,corrmat['房价'])
# plt.rcParams['font.family'] = 'serif'  # 字体族  
# plt.rcParams['font.serif'] = ['Times New Roman']  # 具体字体  
plt.rcParams['font.size'] = 8  # 字体大小

# seaborn.set(font=myfont.get_name()) #函数弃用
# seaborn.heatmap(corrmat,square=True,cmap='YlGnBu',xticklabels=True,yticklabels=True)
plt.show()


#展示其中一个特征与房价的关系
plt.title('房间总数-房价(相关系数0.5)')
seaborn.boxplot(x=df['房间总数'],y=df['房价'])
plt.show()

plt.title('材料和质量-房价(相关系数0.8)')
seaborn.boxplot(x=df['材料和质量'],y=df['房价'])
plt.show()
