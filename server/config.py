from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from datetime import timedelta
from flask_cors import CORS
from os import environ

load_dotenv()

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zodiac.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

#! Flask JWT Extended configuration
app.config["JWT_SECRET_KEY"] = environ.get("JWT_SECRET")
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_CSRF_IN_COOKIES"] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=160)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=90)
GOOGLE_CLIENT_ID = environ.get("GOAUTH_CID")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, prefix="/api/v1")
ma = Marshmallow(app)
flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
