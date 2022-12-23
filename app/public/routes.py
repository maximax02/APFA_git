from . import public_bp
from flask import render_template, session, url_for, redirect, flash
from flask_login import login_required, current_user

from app.public.models import Lista, Padron, Modal
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
    datosModal = {}
    d2 = []
    datosModal[f'modal'] = []
    datosModal[f'imagen'] = []
    # datosJS = {}
    for l in listas:
        # datosModal.append()
        datosModal[f'modal'].append(f'modal{l.id}')
        datosModal[f'modal'].append(f'cancelar-btn{l.id}')
        datosModal[f'modal'].append(f'continuar-btn{l.id}')

        datosModal[f'imagen'].append(f'imagen{l.id}')
        datosModal[f'imagen'].append(f'/apfa/votar/{l.id}')
        datosModal[f'imagen'].append(f'modal{l.id}')

    for l in listas:
        modal = Modal(f'modal{l.id}', f'imagen{l.id}', f'cancelar-btn{l.id}', f'continuar-btn{l.id}', f'/apfa/votar/{l.id}')
        d2.append(modal)

    print(f'DATOS_MODAL: {datosModal}')
    # print(f'DATOS IMAGEN{datos["imagen"]}')
    return render_template('voto.html', listas=listas, datosModal=datosModal, largo=len(listas), d2=d2)

@public_bp.route('/apfa/votar/<int:id_lista>')
@login_required
def voto_realizado(id_lista):
    if current_user.ya_voto:
        flash('Ya votaste, no te hagas el loco')
        return redirect(url_for('public.micuenta'))
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
    users_habilitados = User.query.filter_by(habilitado=True).all()
    print(users_habilitados)
    users_ya_votaron = len(list(filter(lambda user: user.ya_voto, users_habilitados)))
    porcentaje_votos = '{:.2f}'.format( (users_ya_votaron*100)/len(users_habilitados) )
    porcentaje_habilitados = '{:.2f}'.format(((len(users)*100)/len(padron)))

    #TODO: Mostrar ganador parcial.

    datos = {'porcentaje_habilitados': porcentaje_habilitados, 'porcentaje_votos': porcentaje_votos, 'padron': len(padron), 'users_habilitados': len(users_habilitados), 'listas': listas}
    return render_template('resultados.html', datos=datos)
