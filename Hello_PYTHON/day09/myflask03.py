from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Flask!'


@app.route('/forward', methods = ['POST', 'GET']) 
def user():
    a = 999
    list = [['1','1','1','1'],['2','2','2','2']]
    return render_template('myflask03.html', variable = a, list = list)

if __name__ == '__main__':
    app.run(debug=True)