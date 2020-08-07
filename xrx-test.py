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

app = Flask(__name__, template_folder= r'E:/facecard/templates')
# @app.route('/')#主页
# def zhuye():
#     print("hi")
#     return render_template('index.html')

@app.route('/season',methods=["GET"])
def season():
    print("season")
    return render_template('season.html')

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5000)
    app.run()
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    print("* Running on http://127.0.0.1:5000/ ")
    http_server.serve_forever()
