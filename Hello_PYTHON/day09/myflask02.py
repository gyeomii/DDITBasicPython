from flask import Flask, request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Hello, Flask!'


@app.route('/gugu') 
def user():
    param = request.args.get('dan')
    dan = int(param)
    """html태그를 사용할 수 있다."""
    msg = "<table border='1px'>"
    msg+= f"<tr><th>{dan}단</th></tr>"
    for i in range(1,9+1):
        msg+="<tr>"
        msg += f'<td>{dan} * {i} = {dan*i} </td>'
        msg+="</tr>"
    msg +="</table>"
    return msg

if __name__ == '__main__':
    app.run(debug=True)
