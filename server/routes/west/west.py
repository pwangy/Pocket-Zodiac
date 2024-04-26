from .. import request, Resource, login_required, West, west_schema, wests_schema, db

class West(Resource):
    # @login_required
    def get(self):
        try:
            serialized_east = wests_schema.dump(West.query)
            return serialized_east, 200
        except Exception as e:
            return str(e), 400
