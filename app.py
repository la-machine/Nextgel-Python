from flask import jsonify, request, Flask
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn =None
    try:
        conn =sqlite3.connect("GestSchool.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route("/school", methods=["GET","POST"])

def school():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM School")
        school = [
            dict(id_school=row[0],name=row[1],date=row[2],info=row[3])
            for row in cursor.fetchall()
        ]
        if school is not None:
            return jsonify(school)

    if request.method == "POST":
        request.form = request.get_json()
        new_name = request.form["name"]
        new_date = request.form["date"]
        new_info = request.form["info"]
        sql = """INSERT INTO School (name,date,info) VALUES (?,?,?)"""
        cursor = cursor.execute(sql, (new_name,new_date,new_info))

        conn.commit()

        return f"Ecole avce l'id:{cursor.lastrowid} creer avec sucess", 201

@app.route("/virtual", methods=["GET","POST"])

def virtual():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM Virtual ")
        virtual = [
            dict(id_virtual=row[0],name=row[1],info=row[2],id_school=row[3])
            for row in cursor.fetchall()
        ]
        if virtual is not None:
            return jsonify(virtual)

    if request.method == "POST":
        request.form = request.get_json()
        new_name = request.form["name"]
        new_info = request.form["info"]
        new_id_school = request.form["id_school"]
        sql = """INSERT INTO Virtual (name,info,id_school) VALUES (?,?,?)"""
        cursor = cursor.execute(sql, (new_name,new_info,new_id_school))

        conn.commit()

        return f"la salle virtuelle avce l'id:{cursor.lastrowid} creer avec sucess", 201



if __name__=="__main__":
    app.run(debug=True)