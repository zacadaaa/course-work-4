from flask import request
from flask_restx import Resource, Namespace
from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        result = UserSchema(many=True).dump(users)

        return result, 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"users/{user.id}"}

@user_ns.route('/password')
class UpdateUserPasswordViews(Resource):
    def put(self):
        req_json = request.json

        email = req_json.get('email')
        old_password = req_json.get('password_1')
        new_password = req_json.get('password_2')

        user = user_service.get_by_email(email)

        if user_service.compare_password(user.password, old_password):
            user.password = user_service.make_password_hash(new_password)
            result = UserSchema().dump(user)
            user_service.update(result)
        else:
            print("Password did not changed")

        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)

        return result, 200

    def patch(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
