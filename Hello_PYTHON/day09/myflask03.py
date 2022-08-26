from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Flask!'


@app.route('/forward', methods = ['POST', 'GET']) 
def user():
    a = 'forward'
    arrName = ["홍길동", "전우치", "이순신"]
    list = [['1','1','1','1'],['2','2','2','2']]
    dictArr = [
        {'e_id' : '1', 'e_name' : '1', 'sex' : '1', 'addr' : '1'},
        {'e_id' : '2', 'e_name' : '2', 'sex' : '2', 'addr' : '2'}        
    ]
    return render_template('myflask03.html', hgd = a, arrName = arrName, list = list, dictArr = dictArr)

if __name__ == '__main__':
    app.run(debug=True)