from flask import render_template, request, redirect, url_for, session
from conexion import app, db
from models import Nanny
from models import Padres
from werkzeug.utils import secure_filename
import os


app.config['UPLOAD_FOLDER_IMAGES'] = 'static/images'
app.config['UPLOAD_FOLDER_CV'] = 'uploads/cv/'
app.config['UPLOAD_FOLDER_AP'] = 'uploads/antec_policiales/'

@app.route("/")

def index():
    nombre = "¡Poppins! - Cuidamos con Amor"
    return render_template("index.html", nombre = nombre)

# Paso 1 = Creamos el perfil del Login para nuestra niñera

@app.route("/registrar", methods =   ['POST','GET'])
def registrar():

    if request.method   ==  "POST" :
        nombre_y_apellido = request.form['Nombre y Apellido']
        correo =  request.form['Correo electrónico']
        contraseña =  request.form["Ingresar contraseña"]

        datos_padres = Padres(nombre_y_apellido, correo,contraseña)
        
        db.session.add(datos_padres)
        db.session.commit() #Confirmamos la carga de datos aca

        session["padres_id"] = datos_padres.id #aca guardariamos el dato
        return redirect(url_for("mostrar_nanny")) #solucionar a donde nos lleva
    return render_template("registrar.html")

@app.route("/ventana", methods=['GET', 'POST'])

def ventana():
    # Que aca redirija a las niñeras que ofrecen sus servicios en su área
    return render_template("ventana.html")

@app.route('/perfil', methods=['GET', 'POST'])

def perfil():
    if request.method == 'POST':
        # procesamos el formulario donde se guardaran los datos de la niñera
        nombre = request.form["Nombre"]
        apellido = request.form["Apellido"]
        edad = request.form["Edad"]
        cedula = request.form["C.I. Número"]
        ciudad = request.form["Ciudad"]
        descripcion_bio = request.form["Descripción"]
        referencia_personal = request.form["Referencia Personal"]
        numero_rp = request.form["Contacto - Referencia Personal"]
        referencias_laborales1 = request.form["Referencia Laboral 1"]
        numero_rl1 = request.form["Contacto - Referencia Laboral 1"]
        referencias_laborales2 = request.form["Referencia Laboral 2"]
        numero_rl2 = request.form["Contacto - Referencia Laboral 2"]
        tarifa = request.form["Tarifa"]

        # Con estos tres tenemos que pedir que carguen cosas
        foto = request.files["foto"]
        cv = request.files["Inserte su CV"]
        ant_policiales = request.files["Cargue su Antecedente Policial"]
        
        foto_filename = secure_filename(foto.filename)
        foto.save(os.path.join(app.config['UPLOAD_FOLDER_IMAGES'], foto_filename))
        cv_filename = secure_filename(cv.filename)
        ant_policiales_filename = secure_filename(ant_policiales.filename)
        cv.save(os.path.join(app.config['UPLOAD_FOLDER_CV'], cv_filename))
        ant_policiales.save(os.path.join(app.config['UPLOAD_FOLDER_AP'], ant_policiales_filename))

        # Tenemos que guardar esos archivos
        datos_usuario = Nanny(
            nombre=nombre, apellido=apellido, edad=edad, cedula=cedula, ciudad=ciudad, 
            descripcion_bio=descripcion_bio, referencia_personal=referencia_personal, 
            numero_rp=numero_rp, referencias_laborales1=referencias_laborales1, 
            numero_rl1=numero_rl1, referencias_laborales2=referencias_laborales2, 
            numero_rl2=numero_rl2, tarifa=tarifa, foto=foto_filename, cv=cv_filename, ant_policiales=ant_policiales_filename
        )
        
        db.session.add(datos_usuario)
        db.session.commit() #Confirmamos la carga de datos aca

        session["usuario_id"] = datos_usuario.id #aca guardariamos el dato

        return redirect(url_for('confirmacion'))
    return render_template('perfil.html')

# Después, podrías redirigir a una página de confirmación o a otra página de la aplicación
@app.route("/confirmacion", methods=['GET', 'POST'])
def confirmacion():
    return render_template('confirmacion.html')

@app.route('/mostrar_nanny', methods=['GET', 'POST'])
def mostrar_nanny():
    # Recuperar datos de la base de datos
    nannys=Nanny.query.all()
    return render_template('mostrar_nanny.html',  nannys=nannys)

if __name__== "__main__":
    app.run(debug=True)