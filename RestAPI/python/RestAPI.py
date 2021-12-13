from flask import Flask, render_template, request, url_for, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash
from flask_mysqldb import MySQL
from PIL import Image
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

f = open('Users.json')
users = json.load(f)
f.close()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = 'kakka123'
app.config['MYSQL_DB'] = 'databeissi'
mysql = MySQL(app)

@auth.verify_password
def verify_password(username,password):
    if username in users and \
            check_password_hash(users.get(username),password):
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    return render_template('index.html')

@app.route('/click/', methods=['GET','POST'])
@auth.login_required
def click():
    filename = url_for('static', filename='Rotta.jpg')
    cur = mysql.connection.cursor() 
    cur.execute("SELECT trapped FROM rat_intrap")
    state = cur.fetchone()
    print(state)
    
    if state[0] == 1:
        return render_template('index1.html', rotta_image = filename)
    else:
        return render_template('index3.html')
@app.route('/wait/',methods=['GET'])
@auth.login_required
def wait():
    cur = mysql.connection.cursor() 
    cur.execute("SELECT state FROM trap_active")
    state = cur.fetchone()
    print(state)
    cur.close()
    return jsonify({'state': [state]});

@app.route('/r/',methods=['GET','POST'])
@auth.login_required
def reset():
    cur = mysql.connection.cursor()
    cur.execute("UPDATE rat_intrap SET idrat_intrap = %s, trapped = %s",[1,0])
    cur.execute("UPDATE trap_active SET idtrap_active = %s,state = %s",[1,1])
    mysql.connection.commit()
    return render_template('index.html')

@app.route("/img/", methods=["POST"])
@auth.login_required
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    img = img.save(r'static/Rotta.jpg')
    img = Image.open(file.stream)
    cur = mysql.connection.cursor()
    cur.execute("UPDATE rat_intrap SET idrat_intrap = %s, trapped = %s",[1,1])
    cur.execute("UPDATE trap_active SET idtrap_active = %s,state = %s",[1,0])
    mysql.connection.commit()
    cur.close()

    return jsonify({'msg': 'success', 'size': [img.width, img.height]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug = True)