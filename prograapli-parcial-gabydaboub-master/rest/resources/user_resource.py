from flask_restful import Resource, reqparse
from logic.User_logic import UserLogic


class User(Resource):
    def __init__(self):
        self.User_put_args = self.createParser()
        self.logic = UserLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre de la User")
        args.add_argument("contactoEmail", type=str, help="contacto de la User")
        args.add_argument("ingresos", type=int, help="ingresos de la User")
        args.add_argument("egresos", type=int, help="egresos de la User")
        return args

    def head(self, id):
        pass

    def get(self, id):
        result = self.logic.getUserById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def post(self, id):
        result = self.logic.getUserById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def put(self, id):
        User = self.User_put_args.parse_args()
        rows = self.logic.insertUser(User)
        return {"rowsAffefcted": rows}, 200

    def patch(self, id):
        User = self.User_put_args.parse_args()
        rows = self.logic.updateUser(id, User)
        return {"rowsAffefcted": rows}, 200

    def delete(self, id):
        rows = self.logic.deleteUser(id)
        return {"rowsAffefcted": rows}, 200
