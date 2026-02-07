from flask import Flask, render_template, request
import sqlite3
import os
app = Flask(__name__)
def get_db():
    return sqlite3.connect("feedback.db")
@app.route("/")
def home():
    return render_template("feedback.html") 
@app.route("/submit",methods=["POST"])   
def submit():
    name = request.form["name"]   
    email = request.form["email"]
    rating = request.form["rating"]
    feedback = request.form["feedback"] 

    conn = get_db()  
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            rating TEXT,
            feedback TEXT
        )
    """)

    cur.execute(
        "INSERT INTO feedback (name,email,rating,feedback)VALUES(?,?,?,?)",
        (name,email,rating,feedback)
    ) 
    conn.commit()
    conn.close()
    return render_template("success.html")
if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)