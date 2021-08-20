from app import db

class Phishing(db.Model) :
    __tablename__ = 'phishings'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    description = db.Column(db.String())
    timestamp = db.Column(db.DateTime())

    def __init__(self, url, description, datetime) :
        self.url = url
        self.description = description
        self.timestamp = timestamp

    def __repr__(self) :
        return f"<ID {self.id}  , URL {self.url}>"