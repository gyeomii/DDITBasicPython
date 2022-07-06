 from flask import Flask, request,render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Flask!'


@app.route('/para') 
def user():
    parameter_dict = request.args.to_dict()
    if len(parameter_dict) == 0:
        return 'No parameter'

    parameters = ''
    for key in parameter_dict.keys():
        parameters += 'key: {}, value: {}\n'.format(key, request.args[key])
    return parameters

@app.route('/post', methods = ['POST', 'GET']) 
def post():
    if request.method == 'POST':
        result = request.form['id'] #input의 name값을 지정해줘야한다.
        return 'POST : ' + result

@app.route('/dyna')
def dyna():
    return render_template('dyna.html')

if __name__ == '__main__':
    app.run(debug=True)
