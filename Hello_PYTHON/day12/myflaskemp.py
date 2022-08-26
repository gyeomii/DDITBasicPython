from flask import Flask, request, render_template, json
from day12.empdao import EmpDao
from flask.json import jsonify
app = Flask(__name__, static_url_path='')


@app.route('/')
@app.route('/emp', methods = ['POST', 'GET']) 
def index():
    return render_template('emp.html')

@app.route('/ajaxlist', methods=['POST'])
def ajaxlist():
    dao = EmpDao()
    list = dao.selects()
    return jsonify({'empList': list})

@app.route('/ajaxone', methods=['POST'])
def ajaxone():
    eId = request.form['e_id']
    dao = EmpDao()
    emp = dao.select(eId)
    return jsonify({'emp': emp})

@app.route('/ajaxadd', methods=['POST'])
def ajaxadd():
    eName = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    dao = EmpDao()
    cnt = dao.insert(eName, sex, addr)
    return jsonify({"cnt" : cnt})

@app.route('/ajaxmod', methods=['POST'])
def ajaxmod():
    eId = request.form['e_id']
    eName = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    dao = EmpDao()
    cnt = dao.update(eId, eName, sex, addr)
    return jsonify({"cnt" : cnt})

@app.route('/ajaxdel', methods=['POST'])
def ajaxdel():
    eId = request.form['e_id']
    dao = EmpDao()
    cnt = dao.delete(eId)
    return jsonify({"cnt" : cnt})

if __name__ == '__main__':
    app.run(debug=True)