from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

#Definujeme si Flask a SQLalchemy
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#Vytrvorenie databázového súboru na udržiavanie dát
class StatusManager(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userID = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(50), nullable = False)
    body = db.Column(db.String, nullable = False)

db.create_all()





if __name__ == "__main__":
    app.run(debug = True)