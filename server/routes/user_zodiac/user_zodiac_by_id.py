from .. import request, g, Resource, db, user_zodiac_schema

class UserZodiacById(Resource):
    def get(self, id):
        if g.user_zodiac:
            return user_zodiac_schema.dump(g.user_zodiac), 200
        return {"message": f"Could not find User with id #{id}'s signs"}, 404
