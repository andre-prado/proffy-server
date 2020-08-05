from app.main import db
from app.main.model.classe import Classe
from app.main.model.user import User
from app.main.model.class_schedule import ClassSchedule


def convert_schedules(schedules):
    for schedule in schedules:
        week_day = schedule['week_day']
        from_hour = convert_hour_to_minutes(schedule['from'])
        to_hour = convert_hour_to_minutes(schedule['to'])

        return from_hour, to_hour, week_day


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

    new_schedule = ClassSchedule(
        week_day=convert_schedules(data['schedule'])[2],
        from_hour=convert_schedules(data['schedule'])[0],
        to_hour=convert_schedules(data['schedule'])[1],
        classe_id=class_id
    )

    save_changes(new_schedule)

    response_object = {
        'status': 'sucess',
        'message': 'Sucessfully registered.'
    }
    return response_object, 201


def get_all_classes():
    return Classe.query.all()


def get_a_classe(id):
    return Classe.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
    return data.id
