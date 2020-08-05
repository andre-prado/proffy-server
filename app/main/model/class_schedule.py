from .. import db


class ClassSchedule(db.Model):
    """ User Model for storing user related deatails """
    __tablename__ = "class_schedule"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    week_day = db.Column(db.Integer, nullable=False)
    from_hour = db.Column(db.Integer, nullable=False)
    to_hour = db.Column(db.Integer, nullable=False)

    classe_id = db.Column(db.Integer, db.ForeignKey('classe.id'),
                          nullable=False)

    def __repr__(self):
        return f"<ClassSchedule week day:'{self.week_day}\
        ,from:'-{self.from_hour}, to:{self.to_hour}>"
