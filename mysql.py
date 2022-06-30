from flask import Flask,render_template
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'afri'


mysql = MySQL(app)



@app.route('/')
def db():
    cur = mysql.connection.cursor()
    cur.execute(''' SELECT * FROM users ''')
    fetch_data = cur.fetchall()
    cur.close()
    
    
    return render_template('public/db.html',data=fetch_data)


@app.route('/employee')
def emp():
    cur = mysql.connection.cursor()
    cur.execute(''' SELECT * FROM employees ''')
    fetch_data = cur.fetchall()
    cur.close()
    
    
    return render_template('public/emp.html',data=fetch_data)





if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='