from flask import Flask, request, render_template
from day10.empdao import EmpDao
app = Flask(__name__)


@app.route('/')
@app.route('/emp_list', methods = ['POST', 'GET']) 
def index():
    dao = EmpDao()
    emp = dao.selects()
    return render_template('emp_list.html', emp = emp)

@app.route('/emp_detail', methods = ['POST', 'GET']) 
def detail():
    eId = request.args.get('e_id')
    dao = EmpDao()
    emp = dao.select(eId)
    return render_template('emp_detail.html', emp = emp)

@app.route('/emp_add', methods = ['POST', 'GET']) 
def add():
    return render_template('emp_add.html')

@app.route('/emp_add_acts', methods = ['POST', 'GET']) 
def addActs():
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    dao = EmpDao()
    cnt = dao.insert(e_name, sex, addr)
    return render_template('emp_add_acts.html', cnt = cnt)

@app.route('/emp_mod', methods = ['POST', 'GET'])
def emp_mod():
    e_id = request.args.get('e_id')
    dao = EmpDao()
    emp = dao.select(e_id)
    return render_template('emp_mod.html', emp = emp)

@app.route('/emp_mod_acts', methods = ['POST', 'GET'])
def modActs():    
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    dao = EmpDao()
    cnt = dao.update(e_id, e_name, sex, addr)
    return render_template('emp_mod_acts.html', cnt = cnt)

@app.route('/emp_del_acts', methods = ['POST', 'GET'])
def emp_del():
    e_id = request.args.get('e_id')
    dao = EmpDao()
    cnt = dao.delete(e_id)
    return render_template('emp_del_acts.html', cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)