from . import public_bp
from flask import render_template, session, url_for, redirect, flash
from flask_login import login_required, current_user

from app.public.models import Lista, Padron
from app.auth.models import User
from .forms.votar import VotarForm




@public_bp.route('/')
def index():
    # session.clear()
    if current_user.is_authenticated:
        return redirect(url_for('public.micuenta'))
    return render_template('index.html')

@public_bp.route('/apfa/micuenta')
@login_required
def micuenta():

    return render_template('micuenta.html')

@public_bp.route('/apfa/votar')
@login_required
def votar():
    listas = Lista.query.all()
    return render_template('voto.html', listas=listas)

@public_bp.route('/apfa/votar/<int:id_lista>')
@login_required
def voto_realizado(id_lista):
    lista = Lista.query.get(id_lista)
    print(f'VOTANDO A: {lista.num_lista}')
    lista.sumar_voto()
    # current_user.confirmar_voto()
    flash('Voto realizado')
    return redirect(url_for('public.micuenta'))

# @public_bp.route('/apfa/votar', methods=['GET', 'POST'])
# @login_required
# def votar():
#     listas = Lista.query.all()
#     form = VotarForm()
#     form.listas.choices = [(l.id, f'{l.num_lista} - {l.presidente}') for l in listas]
#     if form.validate_on_submit():
#         opcion = form.listas.data
#         lista = Lista.query.get(opcion)
#         lista.sumar_voto()
#         current_user.confirmar_voto()
#         return redirect(url_for('public.micuenta'))
#     return render_template('voto.html', listas=listas, form=form)

@public_bp.route('/apfa/resultados')
def resultados():
    listas = Lista.query.all()
    padron = Padron.query.all()
    users = User.query.all()
    cant_votantes = '{:.2f}'.format(((len(users)*100)/len(padron)))
    print(f'CANT VOTANTES: {cant_votantes}')

    datos = {'cant_votantes': cant_votantes, 'padron': len(padron), 'listas': listas}
    return render_template('resultados.html', datos=datos)
