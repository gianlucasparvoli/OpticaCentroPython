from flask import Flask,render_template, request, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db import Base, Usuarios


engine = create_engine('sqlite:///db\db.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienessomos')
def quienessomos():
    return render_template('quienessomos.html')

@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/login', methods=['GET','POST'])
def login():
    session = DBSession()
    if request.method == 'POST':
        #session.query(Usuarios).filter(Usuarios.Usuario == request.form['Usuario']).all()
        flash('Bienvenido')
        aux = session.query(Usuarios).filter(Usuarios.Usuario == request.form['Usuario']).first()       
        if aux is not None:
            if aux.check_password(request.form['Contraseña']):          
                return render_template('ubicacion.html')
            else:
                flash('Contraseña invalida.')
                return render_template('login.html')
        else:
            flash('No existe el usuario: "%s". Por favor ingrese uno correcto' % (request.form['Usuario']))
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/signin', methods=['GET','POST']) #antiguamente "UsuariosAlta"
def signin():
    #print(request.method)
    session = DBSession()
    if request.method == 'POST':
        aux = session.query(Usuarios).filter(Usuarios.DNI == request.form['DNI']).first()
        if aux is not None:
            flash('Ya existe un usuario con DNI: "%s". Error alta Usuario' % (int(request.form['DNI'])))
            return render_template('signin.html')
        else:
            u = Usuarios(IDGrupo = int(request.form['IDGrupo']),Usuario = request.form['Usuario'],Contraseña = request.form['Contraseña'], Nombre = request.form['Nombre'], Apellido = request.form['Apellido'],DNI = int(request.form['DNI']), Estado = request.form['Estado'])       
            #u = Usuarios(IDGrupo = int(request.form['IDGrupo']),Usuario = request.form['Usuario'],Contraseña = set_password(request.form['Contraseña']), Nombre = request.form['Nombre'], Apellido = request.form['Apellido'],DNI = int(request.form['DNI']), Estado = request.form['Estado'])
            #print(u)
            u.set_password(request.form['Contraseña'])
            session.add(u)
            session.commit()
            session.close()
            flash("Alta correcta")
            return render_template('signin.html')
    else:
        return render_template('signin.html')



if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',debug=True)