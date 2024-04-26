from .. import request, g, Resource, db, element_schema

class ElementById(Resource):
    def get(self, id):
        if g.element:
            return element_schema.dump(g.element), 200
        return {"message": f"Could not find Element with id #{id}"}, 404
