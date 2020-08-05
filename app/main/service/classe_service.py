from app.main import db
from app.main.model.classe import Classe
from app.main.model.user import User
from app.main.model.class_schedule import ClassSchedule


def convert_schedules(schedules, class_id):
    for schedule in schedules:
        week_day = schedule['week_day']
        from_hour = convert_hour_to_minutes(schedule['from'])
        to_hour = convert_hour_to_minutes(schedule['to'])

        new_schedule = ClassSchedule(
            week_day=week_day,
            from_hour=from_hour,
            to_hour=to_hour,
            classe_id=class_id
        )
        save_changes(new_schedule)


def convert_hour_to_minutes(time):
    hour, minute = time.split(':')
    hours = int(hour)
    minutes = int(minute)
    time_in_minutes = (hours * 60) + minutes
    return time_in_minutes


def save_new_classe(data):
    new_user = User(
        name=data['name'],
        avatar=data['avatar'],
        whatsapp=data['whatsapp'],
        bio=data['bio']
    )
    user_id = save_changes(new_user)

    new_classe = Classe(
        subject=data['subject'],
        cost=data['cost'],
        user_id=user_id,
    )
    class_id = save_changes(new_classe)

    convert_schedules(data['schedules'], class_id)

    response_object = {
        'status': 'sucess',
        'message': 'Sucessfully registered.'
    }
    return response_object, 201


def get_all_classes():
    return Classe.query.all()


def get_a_classe(id):
    return Classe.query.filter_by(id=id).first()


def filter_classe(subject):
    return Classe.query.filter_by(subject=subject).all()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    return data.id
