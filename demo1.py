import inline as inline
import xlrd
import xlwt
import pandas as pd
import matplotlib.pyplot as plt
def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('C:\\Users\\wu_08\\Desktop\\sj.csv');
    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    # allSheetNames = workBook.sheet_names();
    # print(allSheetNames);

    # 1.2 按索引号获取sheet的名字（string类型）
    # sheet1Name = workBook.sheet_names()[0];
    # print(sheet1Name);

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    #sheet1_content1 = workBook.sheet_by_index(0); # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    sheet1_content1 = workBook.sheet_by_name('Sheet1');

    # 3. sheet的名称，行数，列数
    #print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);

    # 4. 获取整行和整列的值（数组）
    # rows = sheet1_content1.row_values(3); # 获取第四行内容
    cols = sheet1_content1.col_values(2); # 获取第三列内容
    cols = [int(i) for i in cols]
    print(cols);
    print(type(cols))
    # 5. 获取单元格内容(三种方式)
    # print(sheet1_content1.cell(1, 0).value);
    # print(sheet1_content1.cell_value(2, 2));
    #print(sheet1_content1.row(2)[2].value);
    #print(sheet1_content1.row(3)[2].value);

    # 6. 获取单元格内容的数据类型
    # Tips: python读取excel中单元格的内容返回的有5种类型 [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    #print(sheet1_content1.cell(1, 0).ctype);
    #for n in range(1,9999):
        #i = sheet1_content1.row(n)[2]
    #for i in cols:
    #x = 0  # x个人
    #sheet1_content1.col_values(2) = sheet1_content1.col_values(2).astype(int)  # 将number列的数值类型改为float
    re = [0,0,0]
    def all_list(cols):
        result = {}
        for i in set(cols):
            result[i] = cols.count(i)
        return result
    print(all_list(cols))
    def qsn(cols):
        for i in set(cols):
            for i in range(12,17):
                re[0] = re[0] + cols.count(i)
            return re[0]
    print(qsn(cols))
    def qn(cols):
        for i in set(cols):
            for i in range(18,45):
                re[1] = re[1] + cols.count(i)
            return re[1]
    print(qn(cols))
    def ln(cols):
        for i in set(cols):
            for i in range(46,69):
                re[2] = re[2] + cols.count(i)
            return re[2]
    print(ln(cols))
    print(re)
    # while x <= 9999:
    #     if (n >= 12 and n <= 17):
    #         a = a + 1
    #     elif (n >= 18 and n <= 45):
    #         b = b + 1
    #     elif (n >= 45 and n <= 69):
    #         c = c + 1
    #     x = x + 1
    df = {"人群":["青少年","青年","老年"],"数量":[qsn(cols),qn(cols), ln(cols)]}
    plt.rcParams['font.sans-serif'] = ['SimHei']#用来正常显示中文标签
    plt.pie(df['数量'], labels=df['人群'], explode=None, data=df, shadow=True, autopct='%1.1f%%')
    plt.title('Age segment percentage')
    plt.axis('equal')
    plt.show()
if __name__ == '__main__':
    read_excel();