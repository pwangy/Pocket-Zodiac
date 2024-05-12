from .. import request, g, Resource, db, east_schema, jwt_required

class EastById(Resource):
    @jwt_required()
    def get(self, id):
        if g.east:
            return east_schema.dump(g.east), 200
        return {"error": f"Could not find Eastern sign with id #{id}"}, 404
