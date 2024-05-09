from flask_jwt_extended import current_user
from .. import request, Resource, db, g, user_schema, User, jwt_required
from datetime import datetime


class UserById(Resource):
    # @jwt_required()
    def patch(self, id):
        try:
            # userToUpdate = User.query.filter(User.id == session['user_id']).first()
            if current_user:
                data = request.json
                birthdate_str = data.get('birthdate')
                if not birthdate_str:
                    raise ValueError('Birthdate is required.')
                birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')

                data['birthdate'] = birthdate
                user_data = user_schema.load(data, instance=current_user, partial=True)

                # import ipdb; ipdb.set_trace()
                db.session.commit()
                return user_schema.dump(current_user), 200
            else:
                return {"Error": f"Unable to find user"}, 404
        except Exception as e:
            db.session.rollback()
            return {"Error": str(e)}, 400

    # @jwt_required
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

