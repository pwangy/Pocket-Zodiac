from flask_jwt_extended import current_user
from .. import request, g, Resource, db, UserZodiac, user_zodiac_schema, jwt_required


class UserZodiacById(Resource):
    @jwt_required()
    def get(self, id):
        try:
            user = current_user
            g.zodiac = UserZodiac.query.filter_by(user_id=user.id).first()
            if g.zodiac:
                return user_zodiac_schema.dump(g.user_zodiac), 200
            return {"error": f"Could not find User with id #{id}'s signs"}, 404
        except Exception as e:
            return {"error": str(e)}, 404
