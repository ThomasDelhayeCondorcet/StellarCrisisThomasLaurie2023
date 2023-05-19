from datetime import time
from flask import Flask, render_template, url_for, redirect, session, Response, request, flash
import psycopg2

app = Flask(__name__)
app.config["SECRET_KEY"]="ThomasLaurie2023"

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route("/SignIn", methods=['GET', 'POST'])
def SignIn():
    if request.method=='POST':
        name = request.form['name']
        nickname = request.form['nickname']
        email = request.form['email']
        emailConfirm = 1 if request.form.get('email_checkbox') == "on" else 0
        password = request.form['password']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306", password="graiple56laibla")
        query ="Insert into player (uname, passwd, realname, email, showemail, lastlog, ) VALUES (%s, %s, %s, %s, %s)"
        data = (nickname, password, name, email, emailConfirm)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return render_template("Login.html")
    else:
        return render_template("SignIn.html")

@app.route("/LogIn", methods=['GET', 'POST'])
def LogIn():
    if request.method == 'POST':
        nickname = request.form['nickname']
        password = request.form['password']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "Select * From player WHERE uname =%s AND passwd = %s"
        data = (nickname, password)
        cursor = conn.cursor()
        cursor.execute(query, data)
        user = cursor.fetchone()
        if user is None:
            error = "Username or password are incorrect."
            return render_template("Login.html", error=error)
        else:
            if(user[0] == 1) :
                session["User"] = user
                return render_template("AdminPage.html")
            else:
                session["User"] = user
                return render_template("UserPage.html")

    else:
        return render_template("LogIn.html")

#Function of the admin page
@app.route("/CreateSeries", methods=['GET', 'POST'])
def CreateSeries():
    if request.method == 'POST':
        return render_template("AdminPage.html")
    else:
        return render_template("CreateSeries.html")
@app.route("/ListSeries", methods=['GET', 'POST'])
def ListGames():
    return render_template("ListSeries.html")

@app.route("/YourGames", methods=['GET', 'POST'])
def YourGames():
    return render_template("YourGames.html")

@app.route("/NewGame", methods=['GET', 'POST'])
def NewGame():
    return render_template("NewGame.html")

@app.route("/OpenGames", methods=['GET', 'POST'])
def OpenGames():
    return render_template("OpenGames.html")

@app.route("/Profile", methods=['GET', 'POST'])
def Profile():
    if request.method == 'POST':
        user = session["User"]
        password = request.form["password"]
        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "Update player set passwd = %s WHERE pid=%s"
        data = (password, user[0])
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        success = "password changed successfully"
        return render_template("Profile.html", success=success)
    else:
        return render_template("Profile.html")

@app.route("/Statistics", methods=['GET', 'POST'])
def Statistics():
    return render_template("Statistics.html")

@app.route("/Historic", methods=['GET', 'POST'])
def Historic():
    return render_template("Historic.html")

@app.route("/LogOut")
def LogOut():
    session.clear()
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
