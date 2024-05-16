from .. import (
    request,
    Resource,
    User,
    user_schema,
    create_access_token,
    make_response,
    set_access_cookies,
    create_refresh_token,
    set_refresh_cookies,
    jwt_required,
)


class Login(Resource):
    def post(self):
        try:
            data = request.json
            user = User.query.filter_by(username=data.get("username")).first()

            if user and user.authenticate(data.get("password_hash")):
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(identity=user.id)
                response = make_response(user_schema.dump(user), 200)
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response
            else:
                return {"error": "Invalid login"}, 422
        except Exception as e:
            return {"error": str(e)}, 422
