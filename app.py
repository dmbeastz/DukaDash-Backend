from flask import Flask
from flask_migrate import Migrate
from models import db
import models
from flask_cors import CORS



#Configurations for the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DukaDash.db' 
migrate = Migrate(app, db)


#For initialization of the Flask App
models.db.init_app(app)
















if __name__ == '__main__':
    app.run(debug=True)