from flask import Flask, request,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/kakao')
def kakao():
    return render_template('map_kakao.html')

@app.route('/naver')
def naver():
    return render_template('map_naver.html')

if __name__ == '__main__':
    app.run(debug=True)
