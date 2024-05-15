from utils.calc_e import calc_e_signup
from utils.calc_w import calc_w_signup
from config import app
from .. import (
    request,
    Resource,
    db,
    User,
    user_schema,
    create_access_token,
    make_response,
    set_access_cookies,
    create_refresh_token,
    set_refresh_cookies,
)

class Users(Resource):
    def post(self):
        try:
            data = request.json
            user = user_schema.load(data, partial=True)
            db.session.add(user)
            db.session.commit()

            #? calculate user's western sign
            with app.app_context():
                calc_w_signup(user, app)
                calc_e_signup(user, app)

            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            response = make_response(user_schema.dump(user), 201)
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 422
