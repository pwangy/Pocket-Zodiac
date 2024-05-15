from .. import request, Resource, jwt_required, db, UserZodiac, users_zodiac_schema


class UserZodiac(Resource):
    @jwt_required()
    def get(self):
        try:
            serialized_users_zodiac = users_zodiac_schema.dump(UserZodiac.query)
            return serialized_users_zodiac, 200
        except Exception as e:
            return str(e), 400
