from flask import Flask, redirect, request, render_template, url_for
from server import app, user_input
import csv


@app.route("/", methods=["GET", "POST"])
def index():
	output = ""
	if request.method == "POST":
		dic = {}
		with open('user.csv','r') as csv_in:
			reader = csv.reader(csv_in)	
			for row in reader:
				try:
					if not row[0] in dic:
						dic[row[0]] = row[1]
				except:
					pass
		username = request.form["username"]
		password = request.form["password"]
		if not username in dic:
			output = "Wrong username or password"
			return render_template("index.html",output = output)
		if dic[username] == password:
			return redirect(url_for('home', username = username))
		output = "Wrong username or password"
	return render_template("index.html",output = output)


@app.route("/join", methods=["GET", "POST"])
def join():
	output=''
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		with open('user.csv','r') as csv_in:
			reader = csv.reader(csv_in)		
			for row in reader:
				try:
					if row[0] == username:
						output = "username existed"
						return render_template("join.html", output = output)
				except:
					pass
		with open('user.csv','a') as csv_out:
			writer = csv.writer(csv_out)
			writer.writerow([username, password])
			output = "sign up succeed"
		return redirect(url_for("join", output = output))
	return render_template("join.html", output = output)


@app.route("/home/<username>")
def home(username):
	return render_template("home.html", username = username)


@app.route("/myprofile/<username>")
def myprofile(username):
	list = []
	with open('userprofile.csv','r') as csv_in:
		reader = csv.reader(csv_in)		
		for row in reader:
			try:
				if row[0] == username:
					list.append(row)
			except:
				pass
	return render_template("myprofile.html", list = list)

	
@app.route("/myhistory/<username>")
def myhistory(username):
	list = []
	with open('userhistory.csv','r') as csv_in:
		reader = csv.reader(csv_in)		
		for row in reader:
			try:
				if row[0] == username:
					list.append(row)
			except:
				pass
	return render_template("myhistory.html", list = list)
	

@app.route("/search", methods=["GET", "POST"])
def search():
	list = [1]
	listout = [1]

#	string = request.form["input"]
#	string = string.lower()

#	with open('health.csv','r') as csv_in:
#		reader = csv.reader(csv_in)		
#		for row in reader:
#			list.append(list(row))
	
#	i=0
#	while (i<len(list)):
#		data = list[i].lower()
#		str = data[0]
#		if str.find(string) > 0:
#			listout.append(list[i])
#		i = i+1

#	return redirect(url_for("result", list = listout))
	
	return render_template("search.html")


@app.route("/result")
def result():
	return render_template("result.html", list = list)


@app.route("/main")
def main():
	list =[]
	with open('example.csv','r') as csv_in:
		reader = csv.reader(csv_in)
		for row in reader:
			list.append(row)
	return render_template("main.html", list=list)

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port = 8000)