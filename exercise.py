import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time #时间数据分析
def jijie(cateloge_id):
    plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示统计图中文标签
    df = pd.read_excel('C:/Users/xuanruozunzhe/Desktop/购买记录最终版(2)(1)(1).xlsx',sheet_name='Sheet1')#打开工作簿
    first_quarter = 0
    second_quarter = 0
    third_quarter = 0
    fourth_quarter = 0
    #要查询的商品种类代码
    for x in range(0,df.shape[0]):#遍历所有行
        if str(df.iloc[x,4]) == cateloge_id:
            datatime = df.iloc[x,5]#第6列日期时间数据依次读取
            yuanzu = time.strptime(str(datatime), '%Y%m%d%H%M%S')  # 字符串转时间元组
            year = time.strftime("%Y",yuanzu)  # 时间元组可视化，即将年份读给year
            month = time.strftime("%m", yuanzu)  # 时间元组可视化，即将月份读给month
            if int(month) <= 3:#按照季度累计该种类商品销量
                first_quarter = first_quarter+1
                continue
            if int(month) >= 4 and int(month) <= 6:
                second_quarter = second_quarter+1
                continue
            if int(month) >= 7 and int(month) <= 9:
                third_quarter = third_quarter+1
                continue
            if int(month) >= 10 and int(month) <= 12:
                fourth_quarter = fourth_quarter+1
                continue
    #以下是画图代码
    sales_volumes = [first_quarter,second_quarter,third_quarter,fourth_quarter]#某一季度某一种类商品销售数量列表
    quarter = ['第一季度','第二季度','第三季度','第四季度']#季度数

    #柱状图
    plt.bar(quarter,sales_volumes,color='black',label=cateloge_id)
    plt.title(cateloge_id+'商品'+year+'年各季度销量柱状图')
    plt.ylabel('销量')
    plt.legend()
    plt.savefig("D:/pycharmfinal/untitled/static/test.png")
    plt.show()