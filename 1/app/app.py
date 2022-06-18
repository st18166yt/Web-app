from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import base64
from io import BytesIO
from sympy import *
import cexprtk
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World."

def intg():
    num=1
    x = symbols('x')
    y = symbols('y')
    intg=integrate(num,x)
    min=-5
    max=5
    intg2=integrate(num,(x,-5,5))
    plot(intg,(x,-10,10),title='graph',xlabel='x',ylabel=intg)
    return render_template("intg.html", intg=intg,intg2=intg2,num=num,min=min,
                                        max=max)

@app.route("/top")
def index():
    return render_template("top.html")

@app.route('/next')
def get():
    return render_template("next.html")

@app.route('/intg', methods=['POST'])
def post():
    num = request.form["name"]
    min=0
    max=0
    min = request.form["min"]
    max = request.form["max"]
    x = symbols('x')
    y = symbols('y')
    intg=integrate(num,x)
    intg2=integrate(num,(x,min,max))
    plot(intg,(x,-10,10),title='graph',xlabel='x',ylabel=intg)
    return render_template("intg.html", intg=intg,num=num,intg2=intg2,min=min,
                                        max=max)

@app.route('/sisoku', methods=['POST'])
def spost():
    x1 = int(request.form["x1"])
    y1 = int(request.form["y1"])
    z=x1+y1
    a=x1*y1
    b=x1-y1
    c=x1/y1
    return render_template("sisoku.html",x1=x1,y1=y1,z=z,a=a,b=b,c=c)

@app.route("/practice")
def practice():
    return render_template("practice.html")

@app.route('/practice', methods=['POST'])
def prapost():
    return render_template("practice.html", answer1 = '正解：解の公式',
                            answer2 = '正解：20', answer3 = '正解：7',
                            answer4 = '正解：60', answer5 = '正解：30')

#おまじない
if __name__ == "__main__":
    app.run(debug=True)
