from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Enum

db = SQLAlchemy()

class Nanny(db.Model):
    # insertar atributos de nuestra clase
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column (db.String, nullable=False)
    apellido = db.Column (db.String, nullable=False)
    edad = db.Column (db.String, nullable=False)
    cedula = db.Column (db.Integer, nullable=False)
    ciudad = db.Column (db.String, nullable=False)
    descripcion_bio = db.Column (db.String(100), nullable=False)
    referencia_personal = db.Column (db.String, nullable=False)
    numero_rp = db.Column (db.Integer, nullable=False)
    referencias_laborales1 = db.Column (db.String, nullable=False)
    numero_rl1 = db.Column (db.Integer, nullable=False)
    referencias_laborales2 = db.Column (db.String, nullable=False)
    numero_rl2 = db.Column (db.Integer, nullable=False)
    tarifa = db.Column(db.String, nullable=False)
    foto = db.Column (db.String, nullable=True)
    cv = db.Column (db.String, nullable=True)
    ant_policiales = db.Column (db.String, nullable=False)
    
def __init__ (self, nombre, apellido, edad, cedula, ciudad, habilidades, descripcion_bio, 
              referencia_personal, numero_rp, referencias_laborales1, numero_rl1, 
              referencias_laborales2, numero_rl2, tarifa, foto, cv, ant_policiales):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.cedula = cedula 
    self.ciudad = ciudad
    self.habilidades = habilidades
    self.descripcion_bio = descripcion_bio
    self.referencia_personal = referencia_personal
    self.numero_rp = numero_rp
    self.referencias_laborales1 = referencias_laborales1
    self.numero_rl1 = numero_rl1
    self.referencias_laborales2 = referencias_laborales2
    self.numero_rl2 = numero_rl2
    self.tarifa = tarifa
    self.foto = foto
    self.cv = cv
    self.ant_policiales = ant_policiales

class Padres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_y_apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True)
    contraseña = db.Column(db.String(100), nullable=False)

    def __init__ (self, nombre_y_apellido, correo, contraseña):
        self.nombre_y_apellido = nombre_y_apellido
        self.correo = correo
        self.contraseña = contraseña