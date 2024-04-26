from .. import request, g, Resource, db, west_schema

class WestById(Resource):
    def get(self, id):
        if g.west:
            return west_schema.dump(g.west), 200
        return {"message": f"Could not find Western sign with id #{id}"}, 404
