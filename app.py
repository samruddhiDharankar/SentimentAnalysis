from flask import Flask, render_template, request, redirect, flash, url_for
from textblob import TextBlob

app = Flask(__name__)

@app.route('/result', methods=['GET'])
def dropdown():
    movies = ['ZNMD', 'ABC', 'XYZ', 'UVW']
    return render_template('result.html', movies=movies)

@app.route("/", methods=["POST","GET"])								#LOGIN FUNCTION
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
				# return render_template("result.html", error = error)
			else:
				error = "invalid credentials. Try again"

		return render_template("login.html", error = error)


	except Exception as e:
		# flash(e)
		return render_template("login.html", error = error)


	return render_template("login.html")


@app.route("/result", methods = ["POST", "GET"])						#SENTIMENT ANALYSIS LOGIC
def result():
	result = ""

	if request.method == "POST":
		result = request.form['rating']
			
		blob = TextBlob(result)
		for sentence in blob.sentences:
			result = sentence.sentiment.polarity
			data = result * 100
			data = round(data,2)
			if result > 0:
				return render_template("result1.html", data = data, result="Positive")
			elif result < 0:
				data = (-1) * data
				return render_template("result1.html", data = data, result="Negative")
			else:
				return render_template("result1.html", data = data, result="Neutral")		
		
	else:
		return render_template("result.html")
		

@app.route("/result1", methods = ["POST", "GET"])
def result1():
	return render_template("result1.html")





if __name__ == "__main__":
	app.debug = True
	app.run()
	