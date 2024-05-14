from .. import Resource, unset_access_cookies, make_response, unset_refresh_cookies


class Logout(Resource):
    def delete(self):
        try:
            response = make_response({}, 204)
            unset_access_cookies(response)
            unset_refresh_cookies(response)
            return response
        except Exception as e:
            raise e
