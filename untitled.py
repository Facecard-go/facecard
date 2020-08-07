from flask import Flask,render_template,request,flash
import  pymysql
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import exercise
import exercise1
from flask import Flask, render_template, Response
from gevent.pywsgi import WSGIServer
import time
import cv2
import sys
import os
import time #时间数据分析
app = Flask(__name__, template_folder= r'D:/facecard/templates')
#用户安全问题，设置key值，值随意给出，给的难道越大，破解与麻烦
app.secret_key="13943662109"
#这里是连接虚拟机数据库的代码
# 导入MySQL驱动
@app.route("/zhuce" ,methods=["GET"])
def zhuce():
# 连接mysql，括号内是服务器地址, 端口号, 用户名，密码，存放数据的数据库
    conn = pymysql.connect( host='139.219.8.186',
                        port=3306,
                        user='root',
                        password='123456',
                        database='facecard',
                        charset="utf8")

    cursor = conn.cursor() # Locate the Cursor, all that was required was for buffered to be set to true
    #获得表中有多少条数据
    uname=request.args.get("uname")
    email=request.args.get("email")
    password1=request.args.get("password1")
    password2=request.args.get("password2")
    cursor.execute("insert into myuser(uname,email,password1,password2)values(%s,%s,%s,%s)", [uname,email,password1,password2])
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
    return render_template("login_register.html")
# #向数据库中增加一条数据
# def Insert(value):
#     #连接数据库
#     db=pymysql.connect(
#         host='139.219.8.186',
#         port=3306,
#         user='root',
#         password='123456',
#         database='facecard',
#         charset="utf8"
#     )
#     cursor=db.cursor()
#     sql="insert into myuser(uname,email,password1,password2)values(%s,%s,%s,%s,)"
#     cursor.execute(sql,value)
#     db.commit()
#     db.close()
# #路由,匹配前端请求
# #显示注册界面
# @app.route("/zhuce",methods=["GET"])
# def zhuce():
#     #get获取用户信息
#     uname=request.args.get("uname")
#     email=request.args.get("email")
#     password1=request.args.get("password1")
#     password2=request.args.get("password2")
#
#     while password1 != password2:
#         return render_template("login_register.html")
#     if uname==uname :
#         return "用户名重复，请重新输入"
#
#     if password2 == password1:
#         data = tuple([uname,email,password1,password2])
#         Insert(data)
#         return render_template("zhuye3.html")
#
#
# @app.route("/denglu",methods=["GET"])
# def denglu():
#     # 获取前端提交的用户名和密码
#     uname = request.args.get("uname")
#     email = request.args.get("email")
#     password1 = request.args.get("password1")
#     password2 = request.args.get("password2")
#     print(uname,email,password1,password2)
#     # 到数据库中进行校验
#     conn = pymysql.connect(
#         host='139.219.8.186',
#         port=3306,
#         user='root',
#         password='123456',
#         database='facecard',
#         charset="utf8"
#     )
#     print(conn)
#     cls = conn.cursor()
#     # 前端传递的数据，进行到数据库中进行验证
#     cls.execute("select * from myuser where uname=%s and email=%s and password1=%s and password2=%s", [uname,email,password1,password2])
#     result = cls.fetchone()
#     if result is None:
#         # 用户名和密码不对
#         flash("uname or password1  not  true")
#         return render_template("login_register.html")
#     else:
#         cls.execute("select * from myuser ")
#         result = cls.fetchall()
#         conn.close()
#         return render_template("zhuye3.html", users=result)
#
#
# #接收前端注册界面提交的数据
# @app.route("/sousuo_id",methods=["GET"])
# def sousuo_id():
#     conn = pymysql.connect(host='139.219.8.186',
#                            port=3306,
#                            user='root',
#                            password='123456',
#                            database='facecard',
#                            charset="utf8")
#     cursor = conn.cursor()  # Locate the Cursor, all that was required was for buffered to be set to true
#     # 获得表中有多少条数据
#     sqlcom = "select Category_ID from facecard"  # SQL command
#     aa = cursor.execute(sqlcom)  # Execute the command
#     # 查询表中数据，并以每行一个元祖打印
#     rows = cursor.fetchall()  # 使用 fetchall 函数，将结果集（多维元组）存入 rows 里面
#     # 依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示
#     cursor.close()
#     conn.close()
#     Cateloge_ID=request.args.get("Cateloge_ID")
#     print(Cateloge_ID)
#     return render_template('jijie.html')
#
# @app.route("/doUser")
# def doUser():
#     #获取前端的用户名
#     name = request.args.get("uname")
#     pwd = request.args.get("upwd")
#     print("uname:",name,"upwd:",pwd)
#     #到数据库中添加
#     # 到数据库中进行校验
#     conn = pymysql.connect(
#         host='139.219.8.186',
#         port=3306,
#         user='root',
#         password='123456',
#         database='facecard',
#         charset="utf8"
#     )
#     print(conn)
#     cls = conn.cursor()
#     # 前端传递的数据，进行到数据库中进行验证
#     rows = cls.execute("insert into myuser[name, pwd] values(null,%s ,%s)")
#     conn.commit()
#     if rows>=1:
#         return render_template("login.html")
#     else:
#         return  render_template("register.html")
#
# #显示登录界面
# @app.route("/showLogin")
# def showloign():
#     return  render_template("zhuye3.html")
#
# #画图,endpoint="a"
# @app.route("/jijiesousuo" ,methods=["GET","POST"])
# def showsousuo():
#     return render_template("shangpin.html")
#
# @app.route("/jijie",methods=["POST"])
# def jijie():
#     return render_template("jijie.html")
#
# #检测登录是否成功
# @app.route("/dologin",methods=["POST"])
# def doLogin():
#     #获取前端提交的用户名和密码
#     uname = request.form.get("uname")
#     upwd = request.form.get("upwd")
#     print(uname,upwd)
#     #到数据库中进行校验
#     conn = pymysql.connect(
#         host='139.219.8.186',
#         port=3306,
#         user='root',
#         password='123456',
#         database='facecard',
#         charset="utf8"
#     )
#     print(conn)
#     cls = conn.cursor()
#     #前端传递的数据，进行到数据库中进行验证
#     cls.execute("select * from myuser where uname=%s and upwd=%s",[uname,upwd])
#     result = cls.fetchone()
#     if result is None:
#         #用户名和密码不对
#         flash("user or password  not  true")
#         return render_template("zhuye3.html")
#     else:
#         cls.execute("select * from myuser ")
#         cls.execute("insert into myuser values(null,'uname','upwd')")
#         result = cls.fetchall()
#         conn.close()
#         return render_template("../templates/zhuye3.html",users = result)


# -*- coding: utf-8 -*-



# currPath = sys.path[0]

# 人脸识别模型
# face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_frontalface_default.xml') # 默认模型
# face_cascade = cv2.CascadeClassifier(currPath+'\\haarcascade_profileface.xml')         # 侧脸模型
face_cascade = cv2.CascadeClassifier(r'D:/facecard/haarcascade_frontalface_alt2.xml')  # 正脸模型



# 如果文件不存在则创建
if not os.path.exists('facesData'):
    os.makedirs('facesData')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        # try:
        faces = face_cascade.detectMultiScale(image, 1.3, 5)
        for (x, y, w, h) in faces:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # cv2.imwrite("facesData/"+str(time.time())[:10]+ ".jpg", image[y-40:y+h+40, x-20:x+w+20])
            cv2.imwrite("facesData/" + str(time.time())[:10] + ".jpg", gray[y - 40:y + h + 40, x - 20:x + w + 20])

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.waitKey(100)

        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
@app.route('/')
def zhuye():
    return render_template('index.html')
@app.route('/season')
def season():
    return render_template('season.html')
@app.route('/face')  # 主页
def index():
    # 具体格式保存在index.html文件中
    return render_template('face.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        # 使用generator函数输出视频流， 每次请求输出的类型是image/jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5000)
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    print("* Running on http://127.0.0.1:5000/ ")
    http_server.serve_forever()
    app.run()
    # app.run(debug=True)







#
#
# if __name__ == '__main__':
# app.run()  # 启动服务器
