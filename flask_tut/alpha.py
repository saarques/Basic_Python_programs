from flask import Flask as fsk
from flask import render_template

app = fsk(__name__)


posts = [
	{ "name" : "Gajendra Saraswat", "Class" : "BE 3rd year", "from" : "Bikaner"}, 
	{ "name" : "Anil Choudhary", "Class" : "BTech 2nd year", "from" : "Hissar"}, 
	{ "name" : "Jeeshan Chouhan", "Class" : "BE 3rd year", "from" : "Bikaner"}
	]

@app.route("/")

@app.route("/home")
def home():
	return render_template("home.html", posts = posts)

@app.route("/about")
def about():
	return render_template("about.html", title = "Student Details")

if __name__ == "__main__":
	app.run(debug = True)