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
        name=request.form['name']
        color=request.form['color']
        short_descr=request.form['short_descr']
        long_descr=request.form['long_descr']
        update_time=request.form['update_time']
        time_limit=request.form['time_limit']
        overtime_update_time=request.form['overtime_update_time']
        updates_weekend=request.form['updates_weekend']
        updates_period_from=request.form['updates_period_from']
        updates_period_to=request.form['updates_period_to']
        delay_first_update=request.form['delay_first_update']
        technologies_restricted_allowed=request.form['technologies_restricted_allowed']
        trade_ins_technologies_restricted=request.form['trade_ins_technologies_restricted']
        divider_range_stargate=request.form['divider_range_stargate']
        divider_range_jumpgate=request.form['divider_range_jumpgate']
        max_ship_player=request.form['max_ship_player']
        loss_engineer=request.form['loss_engineer']
        loss_jumpgate=request.form['loss_jumpgate']
        loss_morpher=request.form['loss_morpher']
        loss_carrier=request.form['loss_carrier']
        cost_construction_morpher=request.form['cost_construction_morpher']
        cost_maintenance_morpher=request.form['cost_maintenance_morpher']
        cost_construction_builder=request.form['cost_construction_builder']
        cost_maintenance_builder=request.form['cost_maintenance_builder']
        cost_construction_jumpgate=request.form['cost_construction_jumpgate']
        cost_maintenance_jumpgate=request.form['cost_maintenance_jumpgate']
        cost_construction_carrier=request.form['cost_construction_carrier']
        cost_maintenance_carrier=request.form['cost_maintenance_carrier']
        farming_minimum=request.form['farming_minimum']
        farming_range=request.form['farming_range']
        mineral_minimum=request.form['mineral_minimum']
        mineral_range=request.form['mineral_range']
        fuel_minimum=request.form['fuel_minimum']
        fuel_range=request.form['fuel_range']
        farming_homeworld=request.form['farming_homeworld']
        mineral_homeworld=request.form['mineral_homeworld']
        fuel_homeworld=request.form['fuel_homeworld']
        cost_building_planete=request.form['cost_building_planete']
        population_min_build_ship=request.form['population_min_build_ship']
        number_max_current_game=request.form['number_max_current_game']
        spawn_first=request.form['spawn_first']
        active_bridier=request.form['active_bridier']
        alliance_trade_truce=request.form['alliance_trade_truce']
        number_max_allies=request.form['number_max_allies']
        allow_surrender_draw=request.form['allow_surrender_draw']
        viewable_players=request.form['viewable_players']
        cloakers_invisibles=request.form['cloakers_invisibles']
        constructions_visible=request.form['constructions_visible']
        layout=request.form['layout']
        blind_until_start=request.form['blind_until_start']
        number_max_player=request.form['number_max_player']
        number_systems_min=request.form['number_systems_min']
        number_systems_max=request.form['number_systems_max']
        farming_ratio_max=request.form['farming_ratio_max']
        technology_multiplier=request.form['technology_multiplier']
        initial_technological_level=request.form['initial_technological_level']
        minimum_wins=request.form['minimum_wins']
        maximum_wins=request.form['maximum_wins']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306", password="graiple56laibla")
        query ="Insert into series (sname, color, descr, fulldesc, utime, timelimit, overtime, weekend, fromhr, tohr, udelay, " \
               "availrestrict, tradeinrestrict, stargate, jumpgate, maxship, engloss, jumploss, morphloss, carloss, morpherbuild, " \
               "morphermaint, builderbuild, buildermaint, jumpgatebuild, jumpgatemaint, carrierbuild, carriermaint, avgag, rangeag, " \
               "avgmin, rangemin, avgfuel, rangefuel, homaeag, homemin, homefuel, plabuild, minbuild, max, spawnfirst, bridier, " \
               "blood, maxallies, surrdraw, visp, initcloak, vis, layout, blind, pmax, smin, smax, maxag, tmult, inittech, wins, winmax) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data=(name, color, short_descr, long_descr, update_time, time_limit, overtime_update_time, updates_weekend, updates_period_from,
              updates_period_to, delay_first_update, technologies_restricted_allowed, trade_ins_technologies_restricted, divider_range_stargate,
              divider_range_jumpgate, max_ship_player, loss_engineer, loss_jumpgate, loss_morpher, loss_carrier, cost_construction_morpher,
              cost_maintenance_morpher, cost_maintenance_morpher, cost_construction_builder, cost_maintenance_builder, cost_construction_jumpgate,
              cost_maintenance_jumpgate, cost_construction_carrier, cost_maintenance_carrier, farming_minimum, farming_range, mineral_minimum,
              mineral_range, fuel_minimum, fuel_range, farming_homeworld, mineral_homeworld, fuel_homeworld, cost_building_planete,
              population_min_build_ship, number_max_current_game, spawn_first, active_bridier, alliance_trade_truce, number_max_allies,
              allow_surrender_draw, viewable_players, cloakers_invisibles, constructions_visible, layout, blind_until_start, number_max_player,
              number_systems_min, number_systems_max, farming_ratio_max, technology_multiplier, initial_technological_level, minimum_wins,
              maximum_wins)

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

