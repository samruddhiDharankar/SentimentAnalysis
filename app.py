from flask import Flask, render_template, request, redirect, flash, url_for
from textblob import TextBlob

app = Flask(__name__)



@app.route("/", methods=["POST","GET"])								#LOGIN FUNCTION
def login():
	error = ""
	try:
		if request.method == "POST":
			attempted_username = request.form['username']
			attempted_password = request.form['password']

			if attempted_username == "admin" and attempted_password == "password":
				return redirect(url_for('result'))

			else:
				error = "invalid credentials. Try again"

		return render_template("login.html", error = error)


	except Exception as e:
		# flash(e)
		return render_template("login.html", error = error)


	return render_template("login.html")


@app.route('/result', methods=['GET'])
def dropdown():
    movies = ["Avatar", "Theory of Everything", "Mission Impossible", "Extraction","Ready Player One"] 
    return render_template('result.html', movies=movies)




@app.route("/result", methods = ["POST", "GET"])						#SENTIMENT ANALYSIS LOGIC
def result():
	global average
	
	result = ""
	if request.method == "POST":
		result = request.form['rating']						#value of the rating entered by the user
		select = request.form.get('movies')					#value of the selected movie
		
		blob = TextBlob(result)
		for sentence in blob.sentences:
			result = sentence.sentiment.polarity
			data = result * 100
			data = round(data,2)

			for i in d:
				if i == select:
					average = (average * count[select] + int(data))/(count[select] + 1)
					print("data",data)
					count[select] = count[select] + 1
					d[i] = [average]


			if result > 0:
				return render_template("result1.html", data = data, result="Positive",select = select, average=round(average,2))
			elif result < 0:
				data = (-1) * data
				return render_template("result1.html", data = data, result="Negative",select = select, average=round(average,2))
			else:
				return render_template("result1.html", data = data, result="Neutral",select = select, average=round(average,2))		
		
	else:
		return render_template("result.html")
		


@app.route("/result1", methods = ["POST", "GET"])
def result1():
	return render_template("result1.html")





if __name__ == "__main__":
	average = 0
	keyList = ["Avatar", "Theory of Everything", "Mission Impossible", "Extraction","Ready Player One"] 
	d = {}  
	count = {}
	for i in keyList: 
		d[i] = ""
		count[i] = 0
	
	app.debug = True
	app.run()
	