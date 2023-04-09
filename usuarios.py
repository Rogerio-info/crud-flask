from flask import Blueprint, render_template, request


bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')



@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('usuarios_create.html')