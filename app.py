

from flask import Flask, redirect, render_template,url_for,request
from flask_mysqldb import MySQL


from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)

#config db

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'afri'


mysql = MySQL(app)




#public route
@app.route('/')
def index():
    return render_template('public/public.html')

@app.route('/create')
def create():
    return render_template('public/createorder.html')

@app.route('/dashboard')
def dashboard():
    return render_template('public/dashboard.html')

@app.route('/updateorder')
def updateorder():
    return render_template('public/Updateorder.html')

@app.route('/shipments')
def shipments():
    return render_template('public/shipments.html')








#admin route

@app.route('/login')
def login():
    return render_template('admin/login.html')

@app.route('/register', methods=["POST","GET"])
def register():  
    return render_template('public/register.html')

@app.route('/profile')
def profile():
    return render_template('admin/employee_profile.html')

@app.route('/add', methods=['GET','POST'])
def add():
 
    return render_template('admin/addemployee.html')

@app.route('/update_employee')
def update_employee():
    return render_template('admin/update_employee.html')




def logout():
    render_template('public/public.html')
    
    
    #db check route
    
@app.route('/users')
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