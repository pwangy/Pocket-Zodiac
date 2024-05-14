from flask_jwt_extended import current_user
from .. import request, Resource, db, g, user_schema, User, jwt_required, unset_access_cookies, make_response, unset_refresh_cookies
from datetime import datetime


class UserById(Resource):
    @jwt_required()
    def patch(self, id):
        user = current_user

        try:
            if user:
                data = request.json
                # import ipdb; ipdb.set_trace()
                birthdate_str = data.get('birthdate')
                if not birthdate_str:
                    raise ValueError('Birthdate is required.')

                user_data = user_schema.load(data, instance=user, partial=True)
                db.session.commit()
                return user_schema.dump(user_data), 200
            else:
                return {"error": f"Unable to find user"}, 404
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    @jwt_required()
    def delete(self, id):
        try:
            if user := current_user:
                db.session.delete(user)
                db.session.commit()
                response = make_response({}, 204)
                unset_access_cookies(response)
                unset_refresh_cookies(response)
                return response
            else:
                return {"error": "User not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400
