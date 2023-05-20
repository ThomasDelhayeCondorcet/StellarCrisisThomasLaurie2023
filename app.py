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
                return redirect(url_for("AdminPage"))
            else:
                session["User"] = user
                return redirect(url_for("UserPage"))

    else:
        return render_template("LogIn.html")

#Function of the admin page
@app.route("/AdminPage", methods=['GET', 'POST'])
def AdminPage():
    return render_template("AdminPage.html")
@app.route("/CreateSeries", methods=['GET', 'POST'])
def CreateSeries():
    if request.method == 'POST':
        #Global
        sname=request.form['name']
        descr=request.form['short_descr']
        fulldesc=request.form['long_descr']
        color=request.form['color']
        simage = "empty.gif"
        spawnfirst=request.form['spawn_first']
        max=request.form['number_max_current_game']
        wins=request.form['minimum_wins']
        winmax=request.form['maximum_wins']
        bridier=request.form['active_bridier']

        #Update
        utime=request.form['update_time']
        timelimit=request.form['time_limit']
        overtime=request.form['overtime_update_time']
        weekend=request.form['updates_weekend']
        fromhr=request.form['updates_period_from']
        tohr=request.form['updates_period_to']
        udelay=request.form['delay_first_update']

        #Techno
        availrestrict=request.form['technologies_restricted_allowed']
        tradeinrestrict=request.form['trade_ins_technologies_restricted']
        inittech=request.form['initial_technological_level']
        tmult=request.form['technology_multiplier']

        #Ship
        initcloak=request.form['cloakers_invisibles']
        maxship=request.form['max_ship_player']
        stargate=request.form['divider_range_stargate']
        jumpgate=request.form['divider_range_jumpgate']
        engloss=request.form['loss_engineer']
        jumploss=request.form['loss_jumpgate']
        morphloss=request.form['loss_morpher']
        carloss=request.form['loss_carrier']
        morpherbuild=request.form['cost_construction_morpher']
        morphermaint=request.form['cost_maintenance_morpher']
        builderbuild=request.form['cost_construction_builder']
        buildermaint=request.form['cost_maintenance_builder']
        jumpgatebuild=request.form['cost_construction_jumpgate']
        jumpgatemaint=request.form['cost_maintenance_jumpgate']
        carrierbuild=request.form['cost_construction_carrier']
        carriermaint=request.form['cost_maintenance_carrier']
        plabuild=request.form['cost_building_planet']

        #ore, fuell,..
        avgag=request.form['farming_minimum']
        avgmin=request.form['mineral_minimum']
        avgfuel=request.form['fuel_minimum']
        rangeag=request.form['farming_range']
        rangemin=request.form['mineral_range']
        rangefuel=request.form['fuel_range']
        homeag=request.form['farming_homeworld']
        homemin=request.form['mineral_homeworld']
        homefuel=request.form['fuel_homeworld']
        maxag=request.form['farming_ratio_max']
        minbuild=request.form['population_min_build_ship']
        smin=request.form['number_systems_min']
        smax=request.form['number_systems_max']
        layout=request.form['layout']

        #Other
        pmax=request.form['number_max_player']
        maxallies=request.form['number_max_allies']
        blood=request.form['alliance_trade_truce']
        surrdraw=request.form['allow_surrender_draw']
        blind=request.form['blind_until_start']
        vis=request.form['constructions_visible']
        visp=request.form['viewable_players']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306", password="graiple56laibla")
        query ="Insert into series (sname, descr, fulldesc, color, simage, spawnfirst, max, wins, winmax, bridier, utime, " \
               "timelimit, overtime, weekend, fromhr, tohr, udelay, availrestrict, tradeinrestrict, inittech, tmult, " \
               "initcloak, maxship, stargate, jumpgate, engloss, jumploss, morphloss, carloss, morpherbuild, " \
               "morphermaint, builderbuild, buildermaint, jumpgatebuild, jumpgatemaint, carrierbuild, carriermaint, plabuild, avgag, avgmin, avgfuel, rangeag, " \
               "rangemin, rangefuel, homeag, homemin, homefuel, maxag, minbuild, smin, smax, layout, pmax, maxallies, blood, surrdraw, blind, vis, visp) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data=(sname, descr, fulldesc, color, simage, spawnfirst, max, wins, winmax, bridier, utime, timelimit, overtime, weekend ,fromhr, tohr, udelay,
              availrestrict, tradeinrestrict, inittech, tmult, initcloak, maxship, stargate, jumpgate, engloss, jumploss, morphloss, carloss,
              morpherbuild, morphermaint, builderbuild, buildermaint, jumpgatebuild, jumpgatemaint, carrierbuild, carriermaint, plabuild, avgag, avgmin, avgfuel, rangeag,
              rangemin, rangefuel, homeag, homemin, homefuel, maxag, minbuild, smin, smax, layout, pmax, maxallies, blood, surrdraw, blind, vis, visp)

        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return render_template("AdminPage.html")

    else:
        return render_template("CreateSeries.html")

@app.route("/ListSeries", methods=['GET', 'POST'])
def ListSeries():
    return render_template("ListSeries.html")
# Function for the user page
@app.route("/UserPage", methods=['GET', 'POST'])
def UserPage():
    return render_template("UserPage.html")
@app.route("/ListGames", methods=['GET', 'POST'])
def ListGames():
    if request.method == 'POST':
        return render_template("ListGames.html")
    else:

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
        query = "SELECT * FROM game Join series ON game.sid = series.sid"
        cursor = conn.cursor()
        cursor.execute(query)
        games = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("ListGames.html")


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

