from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL
from PIL import Image
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = 'kakka123'
app.config['MYSQL_DB'] = 'databeissi'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
#    if request.method == "POST":
#        details = request.form
#        firstName = details['fname']
#        lastName = details['fnum']
#        cur = mysql.connection.cursor()
#        cur.execute("INSERT INTO Rotta(nimi, num) VALUES (%s, %s)", (firstName, lastName))
#        mysql.connection.commit()
#        cur.close()


@app.route('/click/', methods=['GET','POST'])
def click():
    filename = url_for('static', filename='Rotta.jpg')
    return render_template('index1.html', rotta_image = filename)

@app.route("/img/", methods=["POST"])
def process_image():
    file = request.files['image']
    img = Image.open(file.stream)
    img = img.save(r'static/Rotta.jpg')
    img = Image.open(file.stream)
    return jsonify({'msg': 'success', 'size': [img.width, img.height]})

	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug = True)