from .. import request, Resource, db, g, user_schema, login_required


class UserById(Resource):
    def get(self, id):
        if g.user:
            return user_schema.dump(g.user), 200
        return {"message": f"Could not find User with id #{id}"}, 404

    @login_required
    def patch(self, id):
        if g.user:
            try:
                data = request.json
                updated_user = user_schema.load(data, instance=g.user, partial=True)
                db.session.commit()
                return user_schema.dump(updated_user), 200
            except Exception as e:
                db.session.rollback()
                return {"message": str(e)}, 422
        return {"message": f"Could not find User with id #{id}"}, 404

    @login_required
    def delete(self, id):
        if g.user:
            db.session.delete(g.user)
            db.session.commit()
            return "", 204
        return {"message": f"Could not find User with id #{id}"}, 404
