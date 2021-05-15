# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:41:40 2021

@author: DRASHTI
"""




from flask import Flask

from flask import Flask, render_template,request, redirect

import pickle
model=pickle.load(open('linear_regression_spark_task1_predict_score.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def main():
    a=""
    return render_template('index.html', data=a)



@app.route('/submit', methods=["POST"])
def submit():
    print("clk")
    a=request.form['time']
    print(a)
    b=model.predict([[int(a)]])
    print(b)
    
    return render_template('index.html', data=b)


if __name__ == "__main__":
    app.run()
    