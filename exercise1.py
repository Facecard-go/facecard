import numpy as np
import pandas as pd
import operator#字典排序
import matplotlib.pyplot as plt#画图

def changxiao():
    plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示统计图中文标签
    df = pd.read_excel('C:/Users/xuanruozunzhe/Desktop/购买记录最终版(2)(1)(1).xlsx',sheet_name='Sheet1')#打开工作簿

    cateloge_id = '1575622'#要查询的商品类型代码
    same_category_id = {}#定义同类型商品不同种类商品空字典

    for i in range(0,df.shape[0]):#遍历所有行
         if str(df.iloc[i,4]) == cateloge_id:#判断第5列是否为要查询的商品类型
             if df.iloc[i,3] not in same_category_id:
                 same_category_id[df.iloc[i,3]] = 1#在商品类型字典中创建一个新的种类并添加一次购买记录
             if df.iloc[i,3] in same_category_id:
                 same_category_id[df.iloc[i,3]] = same_category_id[df.iloc[i,3]]+1#在商品类型字典该种类添加一次购买记录

    ascending_order = sorted(same_category_id.items(),key=operator.itemgetter(1))#按照销量排序输出销量升序列表
    descending_order = []#定义降序空列表
    for i in ascending_order:#升序变降序
        a = ascending_order.pop()
        descending_order.append(a)
    #以下是画图代码
    x = []#横坐标
    y = []#纵坐标
    for i in descending_order:#横纵坐标写入列表
         x.append(str(i[0]))
         y.append(i[1])

    #柱状图
    plt.bar(x[0:8],y[0:8],color='black',label=cateloge_id)
    plt.title(cateloge_id+'各种类销量前8名柱状图')
    plt.ylabel('销量')
    plt.legend()
    plt.savefig("D:/pycharmfinal/untitled/static/test1.png")
    plt.show()
