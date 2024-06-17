from flask import Flask, request, jsonify,Blueprint,make_response
from flask_jwt_extended import JWTManager,jwt_required, create_access_token,get_jwt_identity,create_refresh_token,verify_jwt_in_request
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
import os
from models import db, User,Product,Store,PaymentStatus,Payment,Request
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
import models
from flask.views import MethodView
from datetime import timedelta
import secrets
import string
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_restful import Resource, Api, reqparse
import json
import logging
from werkzeug.utils import secure_filename



profile_bp = Blueprint('profile', __name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DukaDash.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=120) 
app.config['MAIL_SERVER'] = 'smtp.gmail.com' 
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
INVITE_REGISTER_TOKEN = os.environ.get('INVITE_REGISTER_TOKEN')

# Initialize Flask extensions
models.db.init_app(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)
api = Api(app)
migrate = Migrate(app, db)
# Configure CORS
CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["GET", "POST", "PUT", "DELETE"],
    "allow_headers": ["Content-Type", "Authorization"],
    "supports_credentials": True
}})

logging.basicConfig(level=logging.DEBUG)

@app.route('/api/data', methods=["GET", "POST", "PUT", "DELETE"])
def handle_data():
    return 'This is some data from the API.'

