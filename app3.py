from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)
def create_table():
    conn = sqlite3.connect("index3.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)  
    cols=conn.execute("PRAGMA table_info(users)").fetchall()
    col_names=[c[1] for c in cols]
    if "phone" not in col_names:
        conn.execute("ALTER TABLE users ADD COLUMN phone TEXT")       
    conn.commit()
    conn.close() 
create_table()       
@app.route('/')
def home():
    return render_template('index3.html')
@app.route('/validateForm',methods=['GET','POST'])  
def validateForm():
    name=request.form['name'] 
    email=request.form['email'] 
    phone=request.form['phone'] 

    conn=sqlite3.connect("index3.db")
    conn.execute(
        "INSERT INTO users(name,email,phone)VALUES(?,?,?)",
        (name,email,phone)
    )
    conn.commit()
    conn.close()


    return f"Hello {name},your email is {email} , your phone number is {phone}"
    return  "Data saved successfully"
    
if __name__ == '__main__' :
    app.run(debug=True) 

