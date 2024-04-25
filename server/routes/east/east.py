from .. import request, Resource, login_required, East, easts_schema, db

class East(Resource):
    # @login_required
    def get(self):
        try:
            serialized_east = easts_schema.dump(East.query)
            return serialized_east, 200
        except Exception as e:
            return str(e), 400
