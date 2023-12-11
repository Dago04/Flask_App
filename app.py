# Importar los módulos y clases necesarios de Flask y modelos

from flask import Flask, render_template, request, redirect, abort
from models import db, EmpleadoModel


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Empleados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# se instancia la base de datos con el app
db.init_app(app)

# se crean las tablas del modelo


@app.before_request
def create_table():
    db.create_all()


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/crear/empleado', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('crearEmpleado.html')

    if request.method == 'POST':
        empleado_id = request.form['empleado_id']
        nombre = request.form['nombre']
        edad = request.form['edad']
        puesto = request.form['puesto']
        empleado = EmpleadoModel(
            empleado_id=empleado_id, nombre=nombre, edad=edad, puesto=puesto)
        db.session.add(empleado)
        db.session.commit()
        return redirect('/empleados')


@app.route('/empleados')
def listaEmpleados():
    empleados = EmpleadoModel.query.all()
    return render_template('detalist.html', empleados=empleados)


@app.route('/empleados/<int:id>')
def verEmpleado(id):
    empleado = EmpleadoModel.query.filter_by(empleado_id=id).first()
    if empleado:
        return render_template('empleado.html', empleado=empleado)
    return f"Empleado con el id ={id} no existe"


@app.route('/empleados/<int:id>/actualizar', methods=['GET', 'POST'])
def actualizar(id):
    empleado = EmpleadoModel.query.filter_by(empleado_id=id).first()
    if request.method == "POST":
        if empleado:
            db.session.delete(empleado)
            db.session.commit()

            nombre = request.form['nombre']
            edad = request.form['edad']
            puesto = request.form['puesto']
            empleado = EmpleadoModel(
                empleado_id=id, nombre=nombre, edad=edad, puesto=puesto)

            db.session.add(empleado)
            db.session.commit()
            return redirect(f'/empleados/{id}')
        return f'Empleado con el id ={id} no existe'
    return render_template('actualizar.html', empleado=empleado)


@app.route('/empleados/<int:id>/eliminar', methods=['GET', 'POST'])
def eliminarEmpleado(id):
    empleado = EmpleadoModel.query.filter_by(empleado_id=id).first()
    if request.method == 'POST':
        if empleado:
            db.session.delete(empleado)
            db.session.commit()
            return redirect('/empleados')
        abort(404)
    return render_template('eliminarEmpleado.html')


app.run(host='localhost', port=5000)
