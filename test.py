#这里是连接虚拟机数据库的代码
# 导入MySQL驱动
import  pymysql
# 连接mysql，括号内是服务器地址, 端口号, 用户名，密码，存放数据的数据库
conn = pymysql.connect( host='139.219.8.186',
                        port=3306,
                        user='root',
                        password='123456',
                        database='facecard',
                        charset="utf8")

cursor = conn.cursor() # Locate the Cursor, all that was required was for buffered to be set to true
#获得表中有多少条数据
cursor.execute("insert into myuser(uname,email,password1,password2)values()")
print('ok')
sqlcom="select * from myuser" # SQL command
aa=cursor.execute(sqlcom) # Execute the command
print(aa)
#查询表中数据，并以每行一个元祖打印
rows = cursor.fetchall() #使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
for a in rows:
    print(a)
conn.commit()
cursor.close()
conn.close()
