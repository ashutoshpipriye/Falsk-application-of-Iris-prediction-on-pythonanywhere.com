from flask import Flask, render_template, request, session

app = Flask(__name__)
from Classifier import  MyClassifier
app.secret_key = 'any random string'

@app.route('/')
def student():
   return render_template('leaf.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      a	= request.form['sepal-length']
      b = request.form['sepal-width']
      c = request.form['petal-length']
      d = request.form['petal-width']
      inputlist=[a,b,c,d]
      ob=MyClassifier()
      result1=ob.predict(list1=inputlist)
      session['result'] = str(result1)
      return render_template("prediction.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)