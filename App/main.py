from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

#Definujeme si Flask a SQLalchemy
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#Vytrvorenie databázového súboru na udržiavanie dát
class StatusManager(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userID = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(50), nullable = False)
    body = db.Column(db.String, nullable = False)

db.create_all()

#Parser skontorluje vstupné dáta či spĺňajú podmienky, ktoré su v ňom definované
#Automaticky zašle error msg ak nastane problém
put_args = reqparse.RequestParser()
put_args.add_argument("userID", type = int, help = "User ID required!", required = True)
put_args.add_argument("title", type = str, help = "Title required!", required = True)
put_args.add_argument("body", type = str, help = "Body required!", required = True)

update_args = reqparse.RequestParser()
update_args.add_argument("userID", type = int, help = "User ID required!")
update_args.add_argument("title", type = str, help = "Title required!")
update_args.add_argument("body", type = str, help = "Body required!")

#Definovanie podoby dát s, ktorými sa pracuje
resource_field = {
    'id': fields.Integer,
    'userID': fields.Integer,
    'title': fields.String,
    'body': fields.String
    }

#Definovanie requestov API
#marshal_with zoberie vstupné dáta a upravý ich podla definície v resource_fields
class Status(Resource):
    @marshal_with(resource_field)
    def get(self, status_id):
        result = StatusManager.query.filter_by(id=status_id).first()

        if not result:
            abort(404, message = "Could not find status with this ID!")

        return result

    @marshal_with(resource_field)
    def put(self, status_id):
        args = put_args.parse_args()
        result = StatusManager.query.filter_by(id=status_id).first()

        if result:
            abort(409, message = "Status ID taken!")

        status = StatusManager(id = status_id, userID = args['userID'], title = args['title'], body = args['body'])

        db.session.add(status)
        db.session.commit()
        return status, 201
    
    @marshal_with(resource_field)
    def patch(self, status_id):
        args = update_args.parse_args()
        result = StatusManager.query.filter_by(id=status_id).first()

        if not result:
            abort(404, message = "Status does not exist, cannot update!")
        if args['userID']:
            result.userID = args['userID']
        if args['title']:
            result.title = args['title']
        if args['body']:
            result.body = args['body']

        db.session.commit()

        return result

    #def delete(self, video_id):
       # abort_if_video_id_doesnt_exist(video_id)
       # del videos[video_id]
       # return '', 204

#Definovanie kde bude API brať informácie čo má urobiť, za "/" je možné bližšie definovať
#definovať URL, ktorej sa informácie týkajú, momentálne je nastavená na default hodnotu.
api.add_resource(Status, "/status/<int:status_id>")

if __name__ == "__main__":
    app.run(debug = True)