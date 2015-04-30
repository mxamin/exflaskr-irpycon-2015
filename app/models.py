from app import db


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64), nullable=False)
    text = db.Column(db.Text, nullable=False)
