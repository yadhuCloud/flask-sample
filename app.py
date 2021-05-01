import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!");   

@app.route('/syam')
def syam_esult():
   dict = {'Physics':50,'Chemistry':60,'Maths':70}
   return render_template('result.html', result = dict)

@app.route('/clint')
def clint_result():
   dict = {'Physics':46,'Chemistry':70,'Maths':60}
   return render_template('result.html', result = dict)

@app.route('/hari')
def hari_result():
   dict = {'Physics':55,'Chemistry':60,'Maths':70}
   return render_template('result.html', result = dict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
