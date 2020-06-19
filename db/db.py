import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, CheckConstraint, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


Base = declarative_base()


class Grupos(Base):
    __tablename__ = 'Grupos'
    # Columnas de la tabla Grupos
    ID = Column(Integer, primary_key=True, autoincrement=False, nullable=False)
    NivelAcceso = Column(Integer, nullable=False)

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    # Columnas de la tabla Usuarios
    ID = Column(Integer, primary_key=True, nullable=False)
    IDGrupo = Column(Integer, ForeignKey('Grupos.ID'))
    Usuario = Column(String(20), nullable=True)
    Contraseña = Column(String(20), nullable=True)
    Nombre  = Column(String(30), nullable=True)
    Apellido = Column(String(30), nullable=True)
    DNI = Column(Integer, nullable=True)
    Estado = Column(String(3), CheckConstraint("(Estado = 'ACT' OR Estado ='INA')"), nullable=False)
    grupo = relationship(Grupos)

    def set_password(self, password):
        self.Contraseña = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Contraseña, password)
    
class Clientes(Base):
    __tablename__ = 'Clientes'
    # Columnas de la tabla Clientes
    ID = Column(Integer, primary_key=True, nullable=False)
    Nombre  = Column(String(30), nullable=True)
    Apellido  = Column(String(30), nullable=True)
    DNI = Column(Integer, unique=True, nullable=False)
    FechaNac = Column(Date, nullable=True)
    Domicilio = Column(String(50), nullable=True)
    Telefono = Column(String(50), nullable=True)

class Doctores(Base):
    __tablename__ = 'Doctores'
    # Columnas de la tabla Doctores
    ID = Column(Integer, primary_key=True, nullable=False)
    Nombre  = Column(String(30), nullable=True)
    Apellido  = Column(String(30), nullable=True)
    Direccion = Column(String(50), nullable=True)
    Telefono = Column(String(50), nullable=True)


class Pedidos(Base):
    __tablename__ = 'Pedidos'
    # Columnas de la tabla Pedidos
    ID = Column(Integer, primary_key=True, nullable=False)
    NroPedido  = Column(Integer, nullable=True)
    TipoPedido = Column(String(2), CheckConstraint("(TipoPedido = 'SL' OR TipoPedido ='SC' OR TipoPedido ='CL')"), nullable=False)
    IDClientes = Column(Integer, ForeignKey('Clientes.ID'))
    Estado = Column(String(3), CheckConstraint("(Estado = 'PEN' OR Estado ='PRO' OR Estado ='CER' OR Estado ='CAN')"), nullable=False)
    FechaReceta = Column(Date, nullable=True)
    IDDoctor = Column(Integer, ForeignKey('Doctores.ID'))
    LejosODEsferico  = Column(String(10), nullable=True)
    LejosODCilindrico  = Column(String(10), nullable=True)
    LejosODCilindricoGrados  = Column(String(10), nullable=True)
    LejosOIEsferico  = Column(String(10), nullable=True)
    LejosOICilindrico  = Column(String(10), nullable=True)
    LejosOICilindricoGrados  = Column(String(10), nullable=True)
    CercaODEsferico  = Column(String(10), nullable=True)
    CercaODCilindrico  = Column(String(10), nullable=True)
    CercaODCilindricoGrados  = Column(String(10), nullable=True)
    CercaOIEsferico  = Column(String(10), nullable=True)
    CercaOICilindrico  = Column(String(10), nullable=True)
    CercaOICilindricoGrados  = Column(String(10), nullable=True)
    Tipo = Column(String(3), CheckConstraint("(Tipo = 'STO' OR Tipo ='LAB')"), nullable=False)
    Armazon = Column(String(100), nullable=True)
    Modelo = Column(String(100), nullable=True)
    DistInterpLejosOD  = Column(String(10), nullable=True)
    DistInterpLejosOI  = Column(String(10), nullable=True)
    DistInterpCercaOD  = Column(String(10), nullable=True)
    DistInterpCercaOI  = Column(String(10), nullable=True)
    AltBifOD  = Column(String(10), nullable=True)
    AltBifOI  = Column(String(10), nullable=True)
    AltProgOD  = Column(String(10), nullable=True)
    AltProgOI  = Column(String(10), nullable=True)
    AltCentroOD  = Column(String(10), nullable=True)
    AltCentroOI  = Column(String(10), nullable=True)
    LenteTipo = Column(String(3), CheckConstraint("(LenteTipo = 'BIF' OR LenteTipo ='PRO' OR LenteTipo ='MON')"), nullable=False)
    IDUsuario = Column(Integer, ForeignKey('Usuarios.ID'))
    cliente = relationship(Clientes)
    doctor = relationship(Doctores)
    usuario = relationship(Usuarios)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# crear el engine para guardar los datos. La BD sqlite es un archivo

engine = create_engine('sqlite:///db.db')

# CON MYSQL
#engine = create_engine('mysql://opticacentro:root@localhost/OpticaCentro')

# Crear todas las tablas en la engine.
# Equivale a Create Table en sql
Base.metadata.create_all(engine)