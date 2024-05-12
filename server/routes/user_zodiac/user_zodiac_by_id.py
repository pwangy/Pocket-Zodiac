from .. import request, g, Resource, db, user_zodiac_schema, jwt_required

class UserZodiacById(Resource):
    @jwt_required()
    def get(self, id):
        try: 
            if g.user_zodiac:
                return user_zodiac_schema.dump(g.user_zodiac), 200
            return {"error": f"Could not find User with id #{id}'s signs"}, 404
        except Exception as e:
            return {"error": str(e)}, 404
