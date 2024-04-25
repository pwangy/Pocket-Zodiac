from .. import request, g, Resource, db, east_schema

class EastById(Resource):
    def get(self, id):
        if g.east:
            return east_schema.dump(g.east), 200
        return {"message": f"Could not find Eastern sign with id #{id}"}, 404
