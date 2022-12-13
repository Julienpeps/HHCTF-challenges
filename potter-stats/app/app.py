from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:b762596d25ea8c5f@db/hhctf'

db = SQLAlchemy(app)

flag = 'HHCTF{y0u\'r3_A_w1ZArD_hArry}'


@app.route('/', methods=['GET','POST'])
def index():
    search = request.args.get('search') or False
    if search:
        try:
            content = db.engine.connect().execute('SELECT * FROM movies WHERE id = ' + str(search)).all()
            if len(content) > 0:
                return render_template('index.html', content=content)
        except Exception as e:
            return make_response(str(e), 500)
    return render_template('index.html')



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            user = db.engine.connect().execute('SELECT * FROM users7693 WHERE username = %s AND password = %s', (request.form['username'], request.form['password'])).all()
            if len(user) > 0:
                return make_response('Good job, here\'s your flag: %s' % flag)
        except:
            pass
        return render_template('login.html', error='Wrong username or password')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)