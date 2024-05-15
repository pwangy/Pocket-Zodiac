from flask_jwt_extended import current_user
from .. import request, Resource, db, g, user_schema, User, jwt_required, unset_access_cookies, make_response, unset_refresh_cookies
from config import app
from datetime import datetime
from utils.calc_e import calc_e
from utils.calc_w import calc_w


class UserById(Resource):
    @jwt_required()
    def patch(self, id):
        user = current_user

        try:
            if user:
                data = request.json
                current_birthdate = user.birthdate
                birthdate_str = data.get('birthdate')
                updated_user = user_schema.load(data, instance=user, partial=True)
                db.session.commit()

                if birthdate_str and birthdate_str is not current_birthdate:
                    db.session.delete(user.user_zodiacs[0])
                    db.session.commit()
                    
                    with app.app_context():
                        calc_w(updated_user, app)
                        calc_e(updated_user, app)

                return user_schema.dump(updated_user), 200
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
