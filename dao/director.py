from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self, filter):
        page = filter.get('page')
        if page is not None:
            return self.session.query(Director).paginate(int(page), per_page=12).items

        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()

        return director

    def update(self, director):
        director = self.get_one(director.get("id"))
        director.name = director.get("name")

        self.session.add(director)
        self.session.commit()

    def delete(self, did):
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
