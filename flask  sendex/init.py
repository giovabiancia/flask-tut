from flask import Flask, render_template, flash, request, url_for, redirect
from content_management import Content

TOPIC_DICT= Content()

app = Flask(__name__)

app.secret_key = "super secret key"

@app.route("/")
def homepage():
    return render_template("main.html")

@app.route('/login/', methods=["GET", "POST"])
def login_page():

    error = ''
    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))

            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)


@app.route('/dashboard/')
def dashboard():
    flash("admin!!!!")
    flash("password!!!!")

    return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)


@app.errorhandler(404)
def page_not_found(e):
        return render_template("500.html", error = str(e))

@app.route('/slashboard/')
def slashboard():
    try:
        return render_template("dashboard.html", TOPIC_DICT = shamwow)
    except Exception as e:
	    return render_template("500.html", error = str(e))


if __name__ == "__main__":
    app.run(debug=True)
