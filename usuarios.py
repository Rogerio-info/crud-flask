from flask import Blueprint, render_template, request
from models import Usuario
from database import db


bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')



@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method=='GET':
        return render_template('usuarios_create.html')
    
    if request.method=='POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        u = Usuario(nome, email, senha)
        db.session.add(u)
        db.session.commit()
        return 'Dados cadastrados com sucesso.'
