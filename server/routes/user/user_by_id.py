from .. import request, Resource, db, g, user_schema, User, login_required, jwt_required


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
        try:
            userToUpdate = User.query.filter(User.id == id).first()
            if userToUpdate:
                data = request.json
                updated_user = user_schema.load(data, instance=userToUpdate, partial=True)
                db.session.commit()
                return user_schema.dump(updated_user), 200
            else:
                return {"Error": f"Unable to find user"}, 404
        except Exception as e:
            return {"Error": str(e)}, 400
        
        # if user := db.session.get(User, id):
        #     try:
        #         data = request.json
        #         updated_user = user_schema.load(data, instance=user, partial=True)
        #         db.session.commit()
        #         return user_schema.dump(updated_user), 202
        #     except Exception as e:
        #         db.session.rollback()
        #         return {"error": str(e)}, 400
        # else: 
        #     return {"message": f"Could not find User with id #{id}"}, 404

    # @jwt_required
    def delete(self, id):
        try:
            if user := db.session.get(User, id):
                db.session.delete(user)
                db.session.commit()
                return {}, 204
            else:
                return {"error": "User not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 400

