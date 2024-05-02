from .. import (
    Resource,
    db,
    User,
    user_schema,
    # jwt_required,
    # current_user
)


class CheckSession(Resource):
    # @jwt_required()
    def get(self):
        # if current_user:
        # import ipdb; ipdb.set_trace()

        if "user_id" in session:
            user = db.session.get(User, session.get("user_id"))
            return user_schema.dump(current_user), 200
        else:
            return {"message": "Please log in"}, 401
