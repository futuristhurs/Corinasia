from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
app = Flask (__corinasia__)
app.secret_key = "secret_key"

# connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="school"
)

@app.route('/')
def index():
    return render_template('index.html')

#home page
@app.route('/')
def home():
    return render_template('home.html')

#login page
app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('dashboard', user=user))
        else:
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

#registration page
@app.route('/register')
def register():
    return render_template('register.html')

#dashboard
@app.route('/dashboard')
def dashboard():
    user = request.args.get('user')
    return render_template('dashboard.html', user=user)

# student dasboard
@app.route('/dashboard/student')
def student_dashboard():
    return render_template('student_dashboard.html')

#teacher dashboard
@app.route('/dashboard/teacher')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')

#admin dashboard
@app.route('/dashboard/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

#logout
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

#about
@app.route('/about')
def about():
    return render_template('about.html')

#contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __corinasia__ == '__main__':
    app.run(debug=True)
