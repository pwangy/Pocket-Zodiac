from datetime import datetime
from models.west import West
# from ..models.west import West


def calc_w(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    birthdate = birthdate.replace(year=2000)

    signs = West.query.all()

    for sign in signs:
        for start_month, start_day, end_month, end_day in sign.dates:
            if (birthdate.month == start_month and birthdate.day >= start_day) or \
                (birthdate.month == end_month and birthdate.day <= end_day):
                return sign.id, sign.name
            return None, None
