from .. import request, Resource, db, g, user_schema, User, login_required


class UserById(Resource):
    @login_required
    def get(self, id):
        try:
            if g.user:
                return user_schema.dump(g.user), 200
        except Exception as e:
            return {"error": str(e)}, 400

    @login_required
    def patch(self, id):
        user = getattr(g, "user", None)
        if user:
            try:
                data = request.json
                updated_user = user_schema.load(data, instance=user, partial=True)
                db.session.commit()
                return user_schema.dump(updated_user), 202
            except Exception as e:
                return {"error": str(e)}, 400
            else: 
                return {"message": f"Could not find User with id #{id}"}, 404

    @login_required
    def delete(self, id):
        if g.user:
            db.session.delete(g.user)
            db.session.commit()
            return "", 204
        return {"message": f"Could not find User with id #{id}"}, 404
