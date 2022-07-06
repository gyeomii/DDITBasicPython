from flask import Flask, request, render_template
from day10.empdao import EmpDao
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, User!'


@app.route('/index', methods = ['POST', 'GET']) 
def index():
    dao = EmpDao()
    emp = dao.selects()
    return render_template('myFlaskEmp.html', emp = emp)

if __name__ == '__main__':
    app.run(debug=True)