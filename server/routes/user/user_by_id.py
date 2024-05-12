from flask_jwt_extended import current_user, get_jwt_identity
from .. import request, Resource, db, g, user_schema, User, jwt_required
from datetime import datetime


class UserById(Resource):
    @jwt_required()
    def patch(self, id):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        try:
            if user:
                data = request.json
                birthdate_str = data.get('birthdate')
                if not birthdate_str:
                    raise ValueError('Birthdate is required.')
                birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')

                data['birthdate'] = birthdate
                user_data = user_schema.load(data, instance=user, partial=True)

                # import ipdb; ipdb.set_trace()
                db.session.commit()
                return user_schema.dump(current_user), 200
            else:
                return {"error": f"Unable to find user"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    @jwt_required
    def delete(self, id):
        try:
            if user := db.session.get(User, id):
                db.session.delete(user)
                db.session.commit()
                return {}, 204
            else:
                return {"error": "User not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400

