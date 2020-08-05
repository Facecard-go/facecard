from flask import Flask,render_template,request,flash
import  pymysql
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import exercise
import exercise1
import time #时间数据分析
app = Flask(__name__)
#用户安全问题，设置key值，值随意给出，给的难道越大，破解与麻烦
app.secret_key="13943662109"
#向数据库中增加一条数据
def Insert(value):
    #连接数据库
    db=pymysql.connect(
        host='139.219.8.186',
        port=3306,
        user='root',
        password='123456',
        database='facecard',
        charset="utf8"
    )
    cursor=db.cursor()
    sql="insert into myuser(uname,email,password1,password2)values(%s,%s,%s,%s,)"
    cursor.execute(sql,value)
    db.commit()
    db.close()
#路由,匹配前端请求
#显示注册界面
@app.route("/zhuce",methods=["GET"])
def zhuce():
    #get获取用户信息
    uname=request.args.get("uname")
    email=request.args.get("email")
    password1=request.args.get("password1")
    password2=request.args.get("password2")

    while password1 != password2:
        return render_template("login_register.html")
    if uname==uname :
        return "用户名重复，请重新输入"

    if password2 == password1:
        data = tuple([uname,email,password1,password2])
        Insert(data)
        return render_template("zhuye3.html")


@app.route("/denglu",methods=["GET"])
def denglu():
    # 获取前端提交的用户名和密码
    uname = request.args.get("uname")
    email = request.args.get("email")
    password1 = request.args.get("password1")
    password2 = request.args.get("password2")
    print(uname,email,password1,password2)
    # 到数据库中进行校验
    conn = pymysql.connect(
        host='139.219.8.186',
        port=3306,
        user='root',
        password='123456',
        database='facecard',
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    # 前端传递的数据，进行到数据库中进行验证
    cls.execute("select * from myuser where uname=%s and email=%s and password1=%s and password2=%s", [uname,email,password1,password2])
    result = cls.fetchone()
    if result is None:
        # 用户名和密码不对
        flash("uname or password1  not  true")
        return render_template("login_register.html")
    else:
        cls.execute("select * from myuser ")
        result = cls.fetchall()
        conn.close()
        return render_template("zhuye3.html", users=result)


#接收前端注册界面提交的数据
@app.route("/sousuo_id",methods=["GET"])
def sousuo_id():
    conn = pymysql.connect(host='139.219.8.186',
                           port=3306,
                           user='root',
                           password='123456',
                           database='facecard',
                           charset="utf8")
    cursor = conn.cursor()  # Locate the Cursor, all that was required was for buffered to be set to true
    # 获得表中有多少条数据
    sqlcom = "select Category_ID from facecard"  # SQL command
    aa = cursor.execute(sqlcom)  # Execute the command
    # 查询表中数据，并以每行一个元祖打印
    rows = cursor.fetchall()  # 使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
    # 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
    cursor.close()
    conn.close()
    Cateloge_ID=request.args.get("Cateloge_ID")
    print(Cateloge_ID)
    return render_template('jijie.html')

@app.route("/doUser")
def doUser():
    #获取前端的用户名
    name = request.args.get("uname")
    pwd = request.args.get("upwd")
    print("uname:",name,"upwd:",pwd)
    #到数据库中添加
    # 到数据库中进行校验
    conn = pymysql.connect(
        host='139.219.8.186',
        port=3306,
        user='root',
        password='123456',
        database='facecard',
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    # 前端传递的数据，进行到数据库中进行验证
    rows = cls.execute("insert into myuser[name, pwd] values(null,%s ,%s)")
    conn.commit()
    if rows>=1:
        return render_template("login.html")
    else:
        return  render_template("register.html")

#显示登录界面
@app.route("/showLogin")
def showloign():
    return  render_template("zhuye3.html")

#画图,endpoint="a"
@app.route("/jijiesousuo" ,methods=["GET","POST"])
def showsousuo():
    return render_template("shangpin.html")

@app.route("/jijie",methods=["POST"])
def jijie():
    return render_template("jijie.html")

#检测登录是否成功
@app.route("/dologin",methods=["POST"])
def doLogin():
    #获取前端提交的用户名和密码
    uname = request.form.get("uname")
    upwd = request.form.get("upwd")
    print(uname,upwd)
    #到数据库中进行校验
    conn = pymysql.connect(
        host='139.219.8.186',
        port=3306,
        user='root',
        password='123456',
        database='facecard',
        charset="utf8"
    )
    print(conn)
    cls = conn.cursor()
    #前端传递的数据，进行到数据库中进行验证
    cls.execute("select * from myuser where uname=%s and upwd=%s",[uname,upwd])
    result = cls.fetchone()
    if result is None:
        #用户名和密码不对
        flash("user or password  not  true")
        return render_template("zhuye3.html")
    else:
        cls.execute("select * from myuser ")
        cls.execute("insert into myuser values(null,'uname','upwd')")
        result = cls.fetchall()
        conn.close()
        return render_template("../templates/zhuye3.html",users = result)

if __name__ == '__main__':
    app.run()#启动服务器
