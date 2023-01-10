import sqlite3

conn = sqlite3.connect("GestSchool.sqlite") 

cursor = conn.cursor() 

sql_school="""CREATE TABLE School(
    id_school integer PRIMARY KEY,
    name  text NOT NULL,
    date date ,
    info text NOT NULL);"""

sql_photo="""CREATE TABLE Image(
    id_photo integer PRIMARY KEY,
    name  text NOT NULL,
    img  text NOT NULL,
    nametype  text NOT NULL,
    id_school integer ,
    CONSTRAINT fk_school FOREIGN KEY (id_school) REFERENCES School(id_school) );"""

sql_virtual="""CREATE TABLE Virtual(
    id_virtual integer PRIMARY KEY,
    name  text NOT NULL,
    info text,
    id_school integer,
    CONSTRAINT fk_school FOREIGN KEY (id_school) REFERENCES School(id_school) );"""
cursor.execute(sql_school)
cursor.execute(sql_photo)
cursor.execute(sql_virtual)