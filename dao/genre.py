from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

        return genre

    def update(self, genre):
        genre = self.get_one(genre.get("id"))
        genre.name = genre.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, id):
        genre = self.get_one(id)

        self.session.delete(genre)
        self.session.commit()

