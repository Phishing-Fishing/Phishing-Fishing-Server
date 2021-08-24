from app import db

class Phishing(db.Model) :
    __tablename__ = 'phishings'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default = db.func.current_timestamp())

    def __init__(self, url) :
        self.url = url

    def save(self) :
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all() :
        return Phishing.query.all()

    def __repr__(self) :
        return f"<ID {self.id}  , URL {self.url}>"