import jwt
from .. import request, Resource, jwt_required, West, wests_schema


class Wests(Resource):
    @jwt_required()
    def get(self):
        try:
            serialized_west = wests_schema.dump(West.query)
            return serialized_west, 200
        except Exception as e:
            return str(e), 400
