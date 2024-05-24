from models import db 

from flask import Flask

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///poppins.db"

app.config["SECRET_KEY"] = "Acro$$TheUniv3rs3_Grupo_7_2024"

db.init_app(app)

with app.app_context():
    db.create_all()

