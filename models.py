from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmpleadoModel(db.Model):
    __tablename__ = "Empleado"

    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer(), unique=True)
    nombre = db.Column(db.String())
    edad = db.Column(db.Integer())
    puesto = db.Column(db.String(80))

    def __init__(self, empleado_id, nombre, edad, puesto):
        self.empleado_id = empleado_id
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

    def __repr__(self):
        return f"{self.nombre}:{self.empleado_id}"
