from datetime import datetime

def calculate_eastern(birthdate):
    # birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
    # # Define eastern signs and their corresponding date ranges
    # eastern_signs = {
    #     'Aries': [(3, 21), (4, 20)],
    #     'Taurus': [(4, 21), (5, 21)],
    #     'Gemini': [(5, 22), (6, 21)],
    #     'Cancer': [(6, 22), (7, 23)],
    #     'Leo': [(7, 24), (8, 23)],
    #     'Virgo': [(8, 24), (9, 23)],
    #     'Libra': [(9, 24), (10, 23)],
    #     'Scorpio': [(10, 24), (11, 22)],
    #     'Sagittarius': [(11, 23), (12, 21)],
    #     'Capricorn': [(12, 22), (1, 20)],
    #     'Aquarius': [(1, 21), (2, 19)],
    #     'Pisces': [(2, 20), (3, 20)]
    # }
    
    # # Check birthdate against each sign's date range
    # for sign, (start_month, start_day), (end_month, end_day) in eastern_signs.items():
    #     if (birthdate.month == start_month and birthdate.day >= start_day) or \
    #        (birthdate.month == end_month and birthdate.day <= end_day):
    #         # Return the sign object or name, depending on your implementation
    #         return sign
    pass

def calculate_west(birthdate):
    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    west = {
            'Aries': {'id': 1, 'dates': [(3, 21), (4, 20)]},
            'Taurus': {'id': 2, 'dates': [(4, 21), (5, 21)]},
            'Gemini': {'id': 3, 'dates': [(5, 22), (6, 21)]},
            'Cancer': {'id': 4, 'dates': [(6, 22), (7, 23)]},
            'Leo': {'id': 5, 'dates': [(7, 24), (8, 23)]},
            'Virgo': {'id': 6, 'dates': [(8, 24), (9, 23)]},
            'Libra': {'id': 7, 'dates': [(9, 24), (10, 23)]},
            'Scorpio': {'id': 8, 'dates': [(10, 24), (11, 22)]},
            'Sagittarius': {'id': 9, 'dates': [(11, 23), (12, 21)]},
            'Capricorn': {'id': 10, 'dates': [(12, 22), (1, 20)]},
            'Aquarius': {'id': 11, 'dates': [(1, 21), (2, 19)]},
            'Pisces': {'id': 12, 'dates': [(2, 20), (3, 20)]}
        }

    for sign, data in west.items():
        for start_month, start_day, end_month, end_day in data['dates']:
            if (birthdate.month == start_month and birthdate.day >= start_day) or \
                (birthdate.month == end_month and birthdate.day <= end_day):

                return data['id'], sign
