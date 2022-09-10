from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#CHANGE THESE
mysql_user = ''
mysql_password = ''
mysql_host = ''
mysql_db = ''
mysql_table = ''

app = Flask(__name__)
mysql = MySQL(app)
app.config['MYSQL_USER'] = mysql_user
app.config['MYSQL_PASSWORD'] = mysql_password
app.config['MYSQL_HOST'] = mysql_host
app.config['MYSQL_DB'] = mysql_db

@app.route('/', methods = ['POST', 'GET'])
def home():
    #retreives data from database and renders index.html
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT * FROM {mysql_table}''')
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html", data = data)

@app.route('/add', methods = ['POST', 'GET'])
def add():
    #retreives data from database and renders index.html
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT * FROM {mysql_table}''')
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html", data = data)

    #handles form requests to add to the list. alters database accordingly
    if request.method == 'POST':
        to_add = request.form['add'].strip()
        cursor = mysql.connection.cursor()
        cursor.execute(f''' INSERT INTO {mysql_table} VALUES(%s)''',(to_add,))
        mysql.connection.commit()
        cursor.close()
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT * FROM {mysql_table}''')
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html", data = data)

@app.route('/remove', methods = ['POST', 'GET'])
def remove():
    #retreives data from database and renders index.html
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT * FROM {mysql_table}''')
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html", data = data)

    #handles form requests to remove from the list. alters database accordingly
    if request.method == 'POST':
        to_remove = request.form['remove']
        cursor = mysql.connection.cursor()
        cursor.execute(f'''  DELETE FROM {mysql_table} WHERE item=(%s); ''',(to_remove,))
        mysql.connection.commit()
        cursor.close()
        cursor = mysql.connection.cursor()
        cursor.execute(f''' SELECT * FROM {mysql_table}''')
        data = cursor.fetchall()
        cursor.close()
        return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run()
