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
    pk_id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, nullable = False)
    id = db.Column(db.Integer, nullable = False)
    title = db.Column(db.String(50), nullable = False)
    body = db.Column(db.String, nullable = False)

db.create_all()

#Parser skontorluje vstupné dáta či spĺňajú podmienky, ktoré su v ňom definované
#Automaticky zašle error msg ak nastane problém
put_args = reqparse.RequestParser()
put_args.add_argument("userId", type = int, help = "User ID required!", required = True)
put_args.add_argument("id", type = int, help = "ID required!", required = True)
put_args.add_argument("title", type = str, help = "Title required!", required = True)
put_args.add_argument("body", type = str, help = "Body required!", required = True)

update_args = reqparse.RequestParser()
update_args.add_argument("userId", type = int, help = "User ID required!")
put_args.add_argument("id", type = int, help = "ID required!", required = True)
update_args.add_argument("title", type = str, help = "Title required!")
update_args.add_argument("body", type = str, help = "Body required!")

del_args = reqparse.RequestParser()
del_args.add_argument("userId", type = int, help = "User ID required!", required = True)

#Definovanie podoby dát s, ktorými sa pracuje
resource_field = {
    'pk_id': fields.Integer,
    'userId': fields.Integer,
    'id': fields.Integer,
    'title': fields.String,
    'body': fields.String
    }

#Definovanie requestov API
#marshal_with zoberie vstupné dáta a upravý ich podla definície v resource_fields
class Status(Resource):
    @app.route('/', methods = ['GET'])
    @marshal_with(resource_field)
    def get(self, status_id):
        result = StatusManager.query.filter_by(pk_id=status_id).first()

        if not result:
            abort(404, message = "Could not find status with this ID!")

        return result
    
    @app.route('/', methods = ['PUT'])
    @marshal_with(resource_field)
    def put(self, status_id):
        args = put_args.parse_args()
        result = StatusManager.query.filter_by(pk_id=status_id).first()

        if result:
            abort(409, message = "Status ID taken!")

        status = StatusManager(pk_id = status_id, userId = args['userId'], id = args['id'], title = args['title'], body = args['body'])

        db.session.add(status)
        db.session.commit()
        return status, 201
    
    @app.route('/', methods = ['PATCH'])
    @marshal_with(resource_field)
    def patch(self, status_id):
        args = update_args.parse_args()
        result = StatusManager.query.filter_by(pk_id=status_id).first()

        if not result:
            abort(404, message = "Status does not exist, cannot update!")
        if args['title']:
            result.title = args['title']
        if args['body']:
            result.body = args['body']

        db.session.commit()
        return result

    @app.route('/', methods = ['DELETE'])
    @marshal_with(resource_field)
    def delete(self, status_id):
        result = StatusManager.query.filter_by(pk_id=status_id).first()

        if not result:
            abort(404, message = "Could not find status with this ID!")

        db.session.delete(result)
        db.session.commit()
        return result

#Definovanie kde bude API brať informácie čo má urobiť, za "/" je možné bližšie definovať
#definovať URL, ktorej sa informácie týkajú, momentálne je nastavená na default hodnotu.
api.add_resource(Status, "/status/<int:status_id>")

if __name__ == "__main__":
    app.run(debug = True)