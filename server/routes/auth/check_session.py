from .. import (Resource, db, User, user_schema, jwt_required, current_user)


class CheckSession(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            import ipdb; ipdb.set_trace()
            return user_schema.dump(current_user), 200
        else:
            return {"message": "Please log in"}, 401
