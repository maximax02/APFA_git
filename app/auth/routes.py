from . import auth_bp
from app import login_manager
from flask import render_template, redirect, url_for, flash, request, session, current_app
from datetime import datetime
from .utils import generate_confirmation_token, confirm_token, send_email

from .models import User
from .forms.register import RegisterForm
from .forms.login import LoginForm
from app.public.models import Padron

from flask_login import LoginManager, current_user, login_user, login_required, logout_user

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

@auth_bp.route('/apfa/reenviar_mail')
@login_required
def enviar_mail():
    if not current_user.habilitado:
        token = generate_confirmation_token(current_user.email)
        confirm_url = url_for('auth.confirm_email', token=token, _external=True)
        html = render_template('activate_register.html', confirm_url=confirm_url)
        send_email(current_user.email, current_app.config['MAIL_SUBJECT'], html)
        flash('Correo enviado')
    return redirect(url_for('public.micuenta'))


@auth_bp.route('/apfa/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        num_socio = form.num_socio.data
        nombre_usuario = form.nombre_usuario.data
        email = form.email.data
        password = form.password.data
        # Compruebo que no hay ya un usuario con ese email y que ya no esté registrado
        usuario = User.get_by_email(email)
        usuario2 = User.get_by_num_socio(num_socio)
        if (usuario is not None) or (usuario2 is not None):
            flash('Socio ya registrado')
        else:
            # Compruebo que esté en el padrón
            padron = Padron.query.filter_by(num_padron=num_socio).first()
            if padron is None:
                flash('Socio no encontrado')
            else:
                # Creo el usuario y lo guardo
                usuario = User(nombre=nombre_usuario, email=email, numero_socio=num_socio)
                usuario.set_password(password)
                usuario.save()

                token = generate_confirmation_token(usuario.email)
                confirm_url = url_for('auth.confirm_email', token=token, _external=True)
                html = render_template('activate_register.html', confirm_url=confirm_url)
                send_email(usuario.email, current_app.config['MAIL_SUBJECT'], html)

                # Dejo al usuario logueado
                login_user(usuario, remember=True)
                # return redirect(url_for('public.index'))
                return render_template('micuenta.html')
    return render_template('register.html', form=form)

@auth_bp.route('/apfa/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('El link de confirmación es invalido o ya expiró.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.habilitado:
        flash('Cuenta ya confirmada. Por favor loguearse.', 'success')
    else:
        user.habilitado = True
        user.email_confirmed_at = datetime.now()
        user.save()

        flash('Has verificado tu email, Gracias!', 'success')
    return redirect(url_for('public.micuenta'))



@auth_bp.route('/apfa/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.index'))
    form = LoginForm()
    if form.validate_on_submit():
        opcion = int(form.opcion.data)
        user = None

        # Logueo al user según la opción que elijió
        if opcion == 0:
            user = User.get_by_email(form.email.data)
        else:
            user = User.get_by_num_socio(form.num_socio.data)

        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            #TODO: nextpage
            return render_template('micuenta.html', form=form)
        else:
            flash('Usuario o contraseña inválido')
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@auth_bp.route('/apfa/logout')
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('public.index'))


