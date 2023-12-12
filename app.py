from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, session, flash
import logging

app = Flask(__name__)
app.secret_key = 'my_secret_key'

app.logger.setLevel(logging.INFO)

@app.route("/", methods=["GET"])
def hello():

    # "Dhruvik"[100]

    # return render_template("first.html")
    data = {'name': 'Dhruvik', 'age':34}

    return jsonify(data)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

@app.route("/information/<name>")
def info(name):
    designation = "BEIT"

    kwargs = {"name": "Bob Smith", "designation": designation}

    return render_template("second.html", **kwargs)


@app.route("/companyInfo/<name>")
def companyInfo(name):
    kwargs = {
        "company": name,
    }
    return render_template("third.html", **kwargs)

@app.route("/planetInfo/")
def planetInfo():
    planets = {
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    }
    
    kwargs = {
        "planets": planets,
    }
    return render_template("forth.html", **kwargs)

@app.route("/login", methods=["GET"])
def login():
    kwargs = {

    }
    return render_template("login.html", **kwargs)

@app.route("/authenticate", methods=["POST"])
def authenticate():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == 'admin' and password == 'admin':

        session['logged_in_user'] = username
        app.logger.info('Dashboard page is loaded..')
        return redirect(url_for("dashboard", username=username))
        #return render_template("dashboard.html", username=username)
    
    else:
        return render_template("login.html", error="True")

@app.route("/dashboard")
def dashboard():
    requests = request.args.to_dict()
    username = ''

    if 'logged_in_user' in session and session['logged_in_user']:
        username = session['logged_in_user']
    else:
        return redirect(url_for('login'))
    
    return render_template("dashboard.html", username=username)

@app.route("/logout")
def logout():
    flash('You have been logged out')
    session.pop('logged_in_user')
    return redirect(url_for('login'))


@app.route("/download")
def download():
    file_name="example.txt"
    return send_file(file_name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
