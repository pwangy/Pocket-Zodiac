from .. import request, Resource, jwt_required, db, Element, elements_schema


class Elements(Resource):
    @jwt_required()
    def get(self):
        try:
            serialized_elements = elements_schema.dump(Element.query)
            return serialized_elements, 200
        except Exception as e:
            return str(e), 400
