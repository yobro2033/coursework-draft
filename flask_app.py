from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/signup')
def signup():
    return render_template('simple_form.html')

@app.route('/tos')
def tos():
	return render_template('termsofservice.html')

@app.route('/create')
def create():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"""	CREATE TABLE Users(
	                                Name VARCHAR(20) NOT NULL,
					Username VARCHAR(50) NOT NULL PRIMARY KEY,
					Password VARCHAR(20) NOT NULL
						  )
			""")
	con.commit()
	return 'CREATE'

@app.route('/insert', methods=['POST'])
def hello():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Users (Name, Email, Password) VALUES (?,?,?)",(name,email,password))
    con.commit()
    return 'Hello ' + name +',<p>Thank you for registering account with us! <p>We have successfully sent you an email to the following address ' + email + '.'

@app.route('/select')
def select():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute("SELECT * FROM Users")
	return str(cur.fetchall())

@app.route('/verify', methods=['POST'])
def verify():
	con = sqlite3.connect('login.db')
	cur = con.cursor()
	cur.execute(	"SELECT * FROM Users WHERE Name=? AND Email=? AND Password=?",
    		       (request.form['name'],request.form['email'],request.form['password']))
	result = cur.fetchall()
	if len(result) == 0:
		return 'Your information submitted is not registered or incorrect!'
	else:
		return 'You are logged in, ' + request.form['name'] + '!'



