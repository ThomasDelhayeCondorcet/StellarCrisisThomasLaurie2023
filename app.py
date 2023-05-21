from datetime import datetime, date

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
        query= "Select * from player WHERE email=%s OR uname=%s"
        data = (email, nickname)
        cursor = conn.cursor()
        cursor.execute(query, data)
        user = cursor.fetchone()
        if(user == None):
            query2 ="Insert into player (uname, passwd, realname, email, showemail) VALUES (%s, %s, %s, %s, %s)"
            data2 = (nickname, password, name, email, emailConfirm)
            cursor2 = conn.cursor()
            cursor2.execute(query2, data2)
            conn.commit()
            return redirect(url_for("LogIn"))
        else:
            error = "Username or email already used"
            return render_template("SignIn.html", error=error)
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
    user = session["User"]
    Broadcast = user[19]
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "Select * From param"
    cursor = conn.cursor()
    cursor.execute(query)
    logmsg = cursor.fetchone()[0]
    return render_template("AdminPage.html", Broadcast=Broadcast, logmsg=logmsg)
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
        return redirect(url_for("AdminPage"))
    else:
        return render_template("CreateSeries.html")

@app.route("/ListSeries", methods=['GET', 'POST'])
def ListSeries():
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "SELECT * FROM series ORDER BY sid"
    cursor = conn.cursor()
    cursor.execute(query)
    series = cursor.fetchall()
    return render_template("ListSeries.html", series=series)

@app.route("/EditSerie/<sid>", methods=['GET', 'POST'])
def EditSerie(sid):
    if request.method=="POST":
        sname = request.form['name']
        descr = request.form['short_descr']
        fulldesc = request.form['long_descr']
        color = request.form['color']
        simage = "empty.gif"
        spawnfirst = request.form['spawn_first']
        max = request.form['number_max_current_game']
        wins = request.form['minimum_wins']
        winmax = request.form['maximum_wins']
        bridier = request.form['active_bridier']

        # Update
        utime = request.form['update_time']
        timelimit = request.form['time_limit']
        overtime = request.form['overtime_update_time']
        weekend = request.form['updates_weekend']
        fromhr = request.form['updates_period_from']
        tohr = request.form['updates_period_to']
        udelay = request.form['delay_first_update']

        # Techno
        availrestrict = request.form['technologies_restricted_allowed']
        tradeinrestrict = request.form['trade_ins_technologies_restricted']
        inittech = request.form['initial_technological_level']
        tmult = request.form['technology_multiplier']

        # Ship
        initcloak = request.form['cloakers_invisibles']
        maxship = request.form['max_ship_player']
        stargate = request.form['divider_range_stargate']
        jumpgate = request.form['divider_range_jumpgate']
        engloss = request.form['loss_engineer']
        jumploss = request.form['loss_jumpgate']
        morphloss = request.form['loss_morpher']
        carloss = request.form['loss_carrier']
        morpherbuild = request.form['cost_construction_morpher']
        morphermaint = request.form['cost_maintenance_morpher']
        builderbuild = request.form['cost_construction_builder']
        buildermaint = request.form['cost_maintenance_builder']
        jumpgatebuild = request.form['cost_construction_jumpgate']
        jumpgatemaint = request.form['cost_maintenance_jumpgate']
        carrierbuild = request.form['cost_construction_carrier']
        carriermaint = request.form['cost_maintenance_carrier']
        plabuild = request.form['cost_building_planet']

        # ore, fuell,..
        avgag = request.form['farming_minimum']
        avgmin = request.form['mineral_minimum']
        avgfuel = request.form['fuel_minimum']
        rangeag = request.form['farming_range']
        rangemin = request.form['mineral_range']
        rangefuel = request.form['fuel_range']
        homeag = request.form['farming_homeworld']
        homemin = request.form['mineral_homeworld']
        homefuel = request.form['fuel_homeworld']
        maxag = request.form['farming_ratio_max']
        minbuild = request.form['population_min_build_ship']
        smin = request.form['number_systems_min']
        smax = request.form['number_systems_max']
        layout = request.form['layout']

        # Other
        pmax = request.form['number_max_player']
        maxallies = request.form['number_max_allies']
        blood = request.form['alliance_trade_truce']
        surrdraw = request.form['allow_surrender_draw']
        blind = request.form['blind_until_start']
        vis = request.form['constructions_visible']
        visp = request.form['viewable_players']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query ="Update series SET sname= %s, descr= %s, fulldesc= %s, color= %s, simage= %s, spawnfirst= %s, max= %s, wins= %s, " \
               "winmax= %s, bridier= %s, utime= %s, timelimit= %s, overtime= %s, weekend= %s, fromhr= %s, tohr= %s, " \
               "udelay= %s, availrestrict= %s, tradeinrestrict= %s, inittech= %s, tmult= %s, initcloak= %s, maxship= %s, " \
               "stargate= %s, jumpgate= %s, engloss= %s, jumploss= %s, morphloss= %s, carloss= %s, morpherbuild= %s, " \
               "morphermaint= %s, builderbuild= %s, buildermaint= %s, jumpgatebuild= %s, jumpgatemaint= %s, carrierbuild= %s, " \
               "carriermaint= %s, plabuild= %s, avgag= %s, avgmin= %s, avgfuel= %s, rangeag= %s, rangemin= %s, rangefuel= %s, " \
               "homeag= %s, homemin= %s, homefuel= %s, maxag= %s, minbuild= %s, smin= %s, smax= %s, layout= %s, pmax= %s, " \
               "maxallies= %s, blood= %s, surrdraw= %s, blind= %s, vis= %s, visp= %s WHERE sid=%s"

        data = ( sname, descr, fulldesc, color, simage, spawnfirst, max, wins, winmax, bridier, utime, timelimit, overtime,
                 weekend, fromhr, tohr, udelay, availrestrict, tradeinrestrict, inittech, tmult, initcloak, maxship, stargate,
                 jumpgate, engloss, jumploss, morphloss, carloss, morpherbuild, morphermaint, builderbuild, buildermaint, jumpgatebuild,
                 jumpgatemaint, carrierbuild, carriermaint, plabuild, avgag, avgmin, avgfuel, rangeag, rangemin, rangefuel, homeag,
                 homemin, homefuel, maxag, minbuild, smin, smax, layout, pmax, maxallies, blood, surrdraw, blind, vis, visp, sid)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return redirect(url_for("ListSeries"))
    else:
        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "Select * FROM series WHERE sid= %s"
        data = (sid,)
        cursor = conn.cursor()
        cursor.execute(query, data)
        serie = cursor.fetchone()
        return render_template("EditSerie.html", serie=serie)
@app.route("/RespawnSerie/<sid>", methods=['GET', 'POST'])
def RespawnSeries(sid):
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "Select * FROM series WHERE sid= %s"
    data = (sid,)
    cursor = conn.cursor()
    cursor.execute(query, data)
    serie = cursor.fetchone()
    cursor.close()
    query2= "Insert into series (sname, descr, fulldesc, color, simage, spawnfirst, max, wins, winmax, bridier, utime, " \
               "timelimit, overtime, weekend, fromhr, tohr, udelay, availrestrict, tradeinrestrict, inittech, tmult, " \
               "initcloak, maxship, stargate, jumpgate, engloss, jumploss, morphloss, carloss, morpherbuild, " \
               "morphermaint, builderbuild, buildermaint, jumpgatebuild, jumpgatemaint, carrierbuild, carriermaint, plabuild, avgag, avgmin, avgfuel, rangeag, " \
               "rangemin, rangefuel, homeag, homemin, homefuel, maxag, minbuild, smin, smax, layout, pmax, maxallies, blood, surrdraw, blind, vis, visp) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
               "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data2=(serie[1], serie[2], serie[3], serie[4], "empty.gif",serie[8], serie[9], serie[10], serie[11], serie[12],
           serie[13], serie[14], serie[15], serie[16], serie[17], serie[18], serie[19], serie[20], serie[21], serie[22],
           serie[23], serie[24], serie[25], serie[26], serie[27], serie[28], serie[29], serie[30], serie[31], serie[32],
           serie[33], serie[34], serie[35], serie[36], serie[37], serie[38], serie[39], serie[40], serie[41],  serie[42],
           serie[43], serie[44], serie[45], serie[46], serie[47], serie[48], serie[49], serie[50], serie[51], serie[52],
           serie[53], serie[54], serie[55], serie[56], serie[57], serie[58], serie[59], serie[60], serie[61])
    cursor2 = conn.cursor()
    cursor2.execute(query2,data2)
    conn.commit()
    return redirect(url_for("ListSeries"))
@app.route("/KillSerie/<sid>")
def KillSerie(sid):
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "DELETE FROM series WHERE sid= %s"
    data= (sid,)
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    return redirect(url_for("ListSeries"))
@app.route("/Broadcast", methods=['GET', 'POST'])
def Broadcast():
    if request.method=='POST':
        user = session["User"]
        message = request.form['message']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        admin_message = "{} Broadcasted at {}: {}".format(user[1], current_time, message)

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306", password="graiple56laibla")
        query="UPDATE player SET bcast = %s"
        data=(admin_message,)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return redirect(url_for("AdminPage"))
    else:
        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query ="SELECT COUNT(*) FROM player"
        cursor = conn.cursor()
        cursor.execute(query)
        nbrPlayer = cursor.fetchone()[0]

        return render_template("BroadCast.html", nbrPlayer= nbrPlayer)
@app.route("/LoginMessage", methods=['GET', 'POST'])
def LoginMessage():
    if request.method=='POST':
        message = request.form['message']
        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "UPDATE param SET loginmsg = %s"
        data = (message,)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return redirect(url_for("AdminPage"))
    else:
        return render_template("LoginMessage.html")
@app.route("/CheckEmpire")
def CheckEmpire():
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "SELECT * FROM player ORDER BY pid"
    cursor = conn.cursor()
    cursor.execute(query)
    Empire=cursor.fetchall()
    return render_template("CheckEmpire.html", Empire=Empire)
@app.route("/EditEmpire/<pid>", methods=['GET', 'POST'])
def EditEmpire(pid):
    if request.method=="POST":
        uname=request.form['uname']
        realname=request.form['realname']
        email=request.form['email']
        showemail= 1 if request.form.get('email_checkbox') == "on" else 0
        passwd=request.form['password']
        cmt=request.form['cmt']
        victory=request.form['victory']
        wins=request.form['wins']
        kills=request.form['kills']
        killed=request.form['killed']
        ruined=request.form['ruined']
        alien=request.form['alien']
        bridieridx=request.form['bridieridx']
        bridierrank=request.form['bridierrank']
        maxepow=request.form['maxepow']
        maxmpow=request.form['maxmpow']

        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "Update player set uname = %s, realname = %s, email = %s, showemail = %s, passwd = %s, cmt = %s, "\
                "victory = %s, wins = %s, kills = %s, killed = %s, ruined = %s, alien = %s, bridieridx = %s, " \
                "bridierrank = %s, maxepow = %s, maxmpow = %s WHERE pid=%s"
        data = (uname, realname, email, showemail, passwd, cmt,
                victory, wins, kills, killed, ruined, alien, bridieridx,
                bridierrank, maxepow, maxmpow, pid)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        return redirect(url_for("CheckEmpire"))
    else:
        conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                                password="graiple56laibla")
        query = "Select * FROM player WHERE pid= %s"
        data = (pid,)
        cursor = conn.cursor()
        cursor.execute(query, data)
        empire = cursor.fetchone()
        return render_template("EditEmpire.html", empire=empire)
@app.route("/KillEmpire/<pid>")
def KillEmpire(pid):
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "DELETE FROM player WHERE pid= %s"
    data= (pid,)
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    return redirect(url_for("CheckEmpire"))

# Function for the user page
@app.route("/UserPage", methods=['GET', 'POST'])
def UserPage():
    user = session["User"]
    Broadcast = user[19]
    conn = psycopg2.connect(host="student.endor.be", port="5433", database="py2306", user="py2306",
                            password="graiple56laibla")
    query = "Select * From param"
    cursor = conn.cursor()
    cursor.execute(query)
    logmsg = cursor.fetchone()[0]
    return render_template("UserPage.html", Broadcast=Broadcast, logmsg=logmsg)
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

