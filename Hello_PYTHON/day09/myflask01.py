from flask import Flask, request
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


if __name__ == '__main__':
    app.run(debug=True)
