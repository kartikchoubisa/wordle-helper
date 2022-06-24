from wordlehelper import db


class WordState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gray = db.Column(db.String(200))
    green = db.Column(db.String(200))
    yellow = db.Column(db.String(200))

    def __repr__(self):
        return f"WordState('{self.gray}', '{self.green}', '{self.yellow}')"