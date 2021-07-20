from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import os
from markupsafe import escape
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=1)

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
					Username VARCHAR(50) NOT NULL PRIMARY KEY,
					Password VARCHAR(20) NOT NULL
						  )
			""")
	con.commit()
	return 'CREATE'

@app.route('/insert', methods=['POST'])
def hello():
    try:
      con = sqlite3.connect('login.db')
      cur = con.cursor()
      username = request.form['username']
      password = request.form['password']
      if email.strip() == "" or password.strip() == "":
        return {'success': False, 'error': "You have not filled in all of the fields."}
      checkPassword = passwordValidator(password)
      if checkpassword['success'] == False:
        print(checkpassword['error'])
        return {'success': False}
      cursor.execute("SELECT Username FROM Users WHERE Username = ?", (username,))
      data = cursor.fetchall()
      while len(data) != 0:
        return {'success': False, 'error': "This username already exists."}
      cur.execute("INSERT INTO Users (Username, Password) VALUES (?,?)",(username,password))
      con.commit()
      return {'success': True, 'error': "Thank for registering account with us!"}
    except Exception as e:
		    return {'success': False, 'error': type(e).___name___}

def passwordValidator(password):
	if len(password) >= 8:
		pass
	else:
		return {'success': False, 'error': "Your password must have at least 8 characters."}
	symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", "/"]
	for symbol in symbols:
		if symbol in password:
			break
	if symbol in password:
		pass
	else:
		return {'success': False, 'error': "Your password must contain at least 1 special character."}
	for char in list(password):
		try:
			int(char)
			hashNumber = True
			break
		except:
			pass
	if hashNumber == True:
		pass
	else:
		return {'success': False, 'error': "Your password must have at least 1 number."}
	capitalChar = False
	for char in list(password):
		if char.isupper() == True:
			capitalChar = True
			break
	if capitalChar == True:
		pass
	else:
		return {'success': False, 'error': "Your password must have at least 1 upper-case."}
	lowCase = False
	for char in list(password):
		if char.islower() == True:
			lowCase = True
			break
	if lowCase == True:
		pass
	else:
		return {'success': False, 'error': "Your password must have at least 1 lower-case."}
	
	
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
	cur.execute(	"SELECT * FROM Users WHERE Username=? AND Password=?",
    		       (request.form['username'],request.form['password']))
	result = cur.fetchall()
	if len(result) == 0:
		return {'success': False, 'error': "The information you entered is incorrect!"}
	else:
		session.permanent = True
		session['username'] = request.form['username']
		return {'success': True, 'error': "Welcome!"}

@app.route('/un')
def un():
	if 'username' in session:
		return 'Logged in as %s' % escape(session['username'])
	return 'You are not logged in'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('un'))
