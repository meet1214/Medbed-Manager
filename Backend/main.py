from flask import Flask,redirect,render_template
#database connection
local_server=True
app=Flask(__name__)
app.secret_key="meetpatel"
@app.route("/")
def home():
    return render_template("index.html")
app.run(debug=True)