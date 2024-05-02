from .. import (
    Resource, 
    # unset_access_cookies, 
    make_response
)


class Logout(Resource):
    def delete(self):
        try:
            # import ipdb

            # ipdb.set_trace()
            response = make_response({}, 204)
            # unset_access_cookies(response)
            return response
        except Exception as e:
            raise e
