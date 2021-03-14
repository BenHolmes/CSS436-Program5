from flask import Flask, render_template, request, redirect
import Reservation

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

name = "Hello"
queryData = ""

@app.route('/')
def default():
	global name
	name = "Welcome"
	return redirect('/index')

@app.route('/index')
def defaultLanding():
	return render_template('index.html', name=name)

@app.route('/reservation', methods = ['POST'])
def loadData():

	firstName = request.form['firstName']
	lastName = request.form['lastName']
	phoneNum = request.form['phoneNum']
	numTable = request.form['numTable']
	Reservation.sendReservation(firstName, lastName, phoneNum, numTable)
	name = "Reservation sent"
	return redirect('/index')

if __name__ == '__main__':
	app.run()