from .. import db


class Classe(db.Model):
    """ User Model for storing user related deatails """
    __tablename__ = "classe"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    class_schedule = db.relationship('ClassSchedule', backref="classe",
                                     lazy="dynamic")

    def __repr__(self):
        return f"<Classe subject:'{self.subject}, cost: {self.cost}'>"
