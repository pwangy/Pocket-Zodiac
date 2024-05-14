from .. import request, db, Resource, User, make_response, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from schemas.user_schema import UserSchema
from google.auth.transport import requests
from google.oauth2 import id_token
from os import environ

user_schema = UserSchema(session=db.session)
CLIENT_ID = environ.get("GOAUTH_CID")

class OAuth(Resource):
    def post(self):
        data = request.json
        token = data.get("id_token")
        if not token:
            return {"error": "Missing ID token"}, 400
        id_token_bytes = token.encode("utf-8")

        try:
            id_info = id_token.verify_oauth2_token(
                id_token_bytes, requests.Request(), CLIENT_ID
            )
            user = User.query.filter_by(email=id_info.get("email")).first()
            if not user:
                user_data = {
                    "username": id_info.get("name"),
                    "email": id_info.get("email"),
                    "password_hash": "TempPass1!",
                    "birthdate": "1977-01-01"
                }
                user_schema.validate(user_data)
                new_user = user_schema.load(user_data, session=db.session)
                db.session.add(new_user)
                db.session.commit()

            final_user = user if user else new_user
            jwt = create_access_token(identity=final_user.id)
            refresh_toekn = create_refresh_token(identity=final_user.id)
            response = make_response(user_schema.dump(final_user), 200 if user else 201)
            set_access_cookies(response, jwt)
            set_refresh_cookies(response, refresh_toekn)
            return response

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400
