from flask import Flask, render_template, request, redirect, flash, url_for
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/result")
def result():
	return render_template("result.html")


@app.route("/login", methods=["POST","GET"])
def login():
	error = ""
	try:
		if request.method == "POST":
			attempted_username = request.form['username']
			attempted_password = request.form['password']

			# flash(attempted_username)
			# flash(attempted_password)

			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for('result'))
			else:
				error = "invalid credentials. Try again"

		return render_template("login.html", error = error)


	except Exception as e:
		# flash(e)
		return render_template("login.html", error = error)


	return render_template("login.html")




if __name__ == "__main__":
	app.debug = True
	app.run()
	