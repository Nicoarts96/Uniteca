from flask import Flask, render_template, request, redirect, jsonify, url_for, session, json
from flask_cors import CORS
from flask_session import Session
from pymongo import MongoClient
from datetime import datetime
import uuid
import os
import secrets

client = MongoClient('mongodb+srv://admin:uniteca123@cluster0.znfxrbr.mongodb.net/test')
db = client["uniteca"]
libb = db["libri"]
utenti = db["utenti"]
reservation = db["reservation"]
UPLOAD_FOLDER = '../uniteca/static/images/'
app = Flask(__name__)
app.secret_key = 'Keyuniteca'
cors = CORS(app)


secret_key = secrets.token_hex(16)
# example output, secret_key = 000d88cd9d90036ebdd237eb6b0db000
app.config['SECRET_KEY'] = secret_key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login_user = utenti.find_one({"Email": request.form['Email']})
        if login_user:
            password = request.form['Password']
            if login_user['Password'] == password:
                session['key'] = 'value'
                session["_id"] = login_user["_id"]
                session['Type'] = login_user['Type']
                if login_user['Type'] == 'admin':
                    return redirect('admin')
                else:
                    return redirect('user')
            else:
                return render_template('index.html', error=2)
        return render_template('index.html', error=3)
    return render_template('index.html')



@app.route('/registration/',methods = ['POST', 'GET'])
def registration():
    if request.method == 'POST':
        emailcheck = request.form['FromEmailAddress']
        if emailcheck.find('studenti.universita.it') == -1:
            return render_template('registration.html', error=3)
        else:
            reg_user = utenti.find_one({"Email": request.form['FromEmailAddress']})
            if reg_user:
                return render_template('registration.html', error=1)
            else:
                pss = request.form['Password']
                if pss == request.form['ConfirmPassword']:
                    utenti.insert_one({"_id": uuid.uuid4().hex, "Name": request.form['Name'], "Surname": request.form['Surname'], "Email": request.form['FromEmailAddress'], "Password": request.form['Password'], "Type": "user"})
                    return render_template('registration.html', succ=1)
                else:
                    return render_template('registration.html', error=2)
    return render_template('registration.html')

#user home page
@app.route('/user',methods = ['POST', 'GET'])
def user():
    usertype = utenti.find_one({'_id': session['_id']})
    if(usertype):
        if session['_id'] != usertype['_id']:
            return render_template('index.html', error=1)
    return render_template('user.html')


#user search_borrow
@app.route('/search_borrow',methods = ['POST', 'GET'])
def search_borrow():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if session['_id'] != user['_id']:
            return render_template('index.html', error=1)
    return render_template('user1.html')


#user book place
@app.route('/book_place',methods = ['POST', 'GET'])
def book_place():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if session['_id'] != user['_id']:
            return render_template('index.html', error=1)
    return render_template('user2.html')


#admin home
@app.route('/admin',methods = ['POST', 'GET'])
def admin():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if user['Type'] == 'admin':
            if session['_id'] == user['_id']:
                return render_template('admin.html')
    return render_template('index.html', error=1)


#admin add/remove book
@app.route('/addrm_book',methods = ['POST', 'GET'])
def addrm_book():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if user['Type'] == 'admin':
            if session['_id'] == user['_id']:
                return render_template('admin1.html')
    return render_template('index.html', error=1)


#admin add a book
@app.route('/add_b/',methods = ['POST', 'GET'])
def add_b():    
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if user['Type'] == 'admin':
            if session['_id'] == user['_id']:
                return render_template('admin1.html')
    return render_template('index.html', error=1)


#admin reservation
@app.route('/reservation',methods = ['POST', 'GET'])
def reservation():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if user['Type'] == 'admin':
            if session['_id'] == user['_id']:
                return render_template('admin2.html')
    return render_template('index.html', error=1)

#admin loaned book
@app.route('/loaned_book',methods = ['POST', 'GET'])
def loaned_book():
    user = utenti.find_one({'_id': session['_id']})
    if(user):
        if user['Type'] == 'admin':
            if session['_id'] == user['_id']:
                return render_template('admin3.html')
    return render_template('index.html', error=1)


@app.route('/search/',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        libro = libb.find_one({"name": request.form['name']})
        if libro:
            return 'trovato'
        else:
            return 'non trovato'

@app.route('/searchoff/',methods = ['POST', 'GET'])
def searchoff():
    if request.method == 'POST':
        libro = libb.find_one({"name": request.form['name']})
        if libro:
            return render_template('books.html')
        else:
            return 'non trovato'


@app.route('/resetpwd',methods = ['POST', 'GET'])
def resetpwd():
    return render_template('resetpwd.html')


#logout
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('_id', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug = True)