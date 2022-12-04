from flask import request
from flask_restx import Resource, Namespace
from decorators import auth_required, admin_required
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    #@auth_required
    def get(self):
        page = request.args.get('page')

        filters = {
            'page': page
        }
        genres = genre_service.get_all(filters)
        result = GenreSchema(many=True).dump(genres)

        return result, 200

    #@admin_required
    def post(self):
        req_json = request.json()
        genre = genre_service.create(req_json)
        return "", 201, {"location": f"genres/{genre.id}"}



@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    #@auth_required
    def get(self, uid):
        genre = genre_service.get_one(uid)
        result = GenreSchema().dump(genre)

        return result, 200

    #@admin_required
    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        genre_service.update(req_json)
        return "", 204

    #@admin_required
    def delete(self, uid):
        genre_service.delete(uid)
        return "", 204
