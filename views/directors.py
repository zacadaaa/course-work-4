from flask import request
from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    #@auth_required
    def get(self):
        page = request.args.get('page')

        filters = {
            'page': page
        }
        directors = director_service.get_all(filters)
        result = DirectorSchema(many=True).dump(directors)

        return result, 200

    #@admin_required
    def post(self):
        req_json = request.json()
        director = director_service.create(req_json)
        return "", 201, {"location": f"directors/{director.id}"}


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    #@auth_required
    def get(self, uid):
        director = director_service.get_one(uid)
        result = DirectorSchema().dump(director)

        return result, 200

    #@admin_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        director_service.update(req_json)

        return "", 204

    #@admin_required
    def delete(self, uid):
        director_service.delete(uid)

        return "", 204
