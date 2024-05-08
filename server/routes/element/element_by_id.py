from .. import request, g, Resource, db, element_schema, jwt_required

class ElementById(Resource):
    @jwt_required()
    def get(self, id):
        try:
            if g.element:
                return element_schema.dump(g.element), 200
            return {"message": f"Could not find Element with id #{id}"}, 404
        except Exception as e:
            return {"error": str(e)}, 400
