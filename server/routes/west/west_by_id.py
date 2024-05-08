from .. import request, g, Resource, db, west_schema, jwt_required

class WestById(Resource):
    @jwt_required()
    def get(self, id):
        try:
            if g.west:
                return west_schema.dump(g.west), 200
            return {"message": f"Could not find Western sign with id #{id}"}, 404
        except Exception as e:
            return {"error": str(e)}, 404
