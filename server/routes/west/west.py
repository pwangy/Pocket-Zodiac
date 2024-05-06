from .. import (request, Resource, login_required, West, wests_schema)

class Wests(Resource):
    @login_required
    def get(self):
        try:
            serialized_west = wests_schema.dump(West.query)
            return serialized_west, 200
        except Exception as e:
            return str(e), 400
