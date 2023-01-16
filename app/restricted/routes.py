from . import restricted_bp

import os
from app import db, admin
from flask_login import current_user, login_required
from flask import render_template, request, url_for, redirect, flash, current_app
from flask_admin.contrib.sqla import ModelView
from flask_user import roles_required
from werkzeug.utils import secure_filename
from .forms.agregar_lista import AgregarListaForm
from PIL import Image


from app.auth.models import User
from app.public.models import Lista, Padron

# Importar los modelos a ver en el admin
from flask_admin import AdminIndexView

class MyModelView(ModelView):
    def is_accessible(self):
        has_auth = current_user.is_authenticated
        role_admin = False
        if has_auth:
            role_admin = current_user.is_admin
        return has_auth and role_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        hola = current_user
        has_auth = current_user.is_authenticated
        role_admin = False
        if has_auth:
            role_admin = current_user.is_admin
        return has_auth and role_admin


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Lista, db.session))
admin.add_view(MyModelView(Padron, db.session))

@restricted_bp.route('/test')
@login_required
@roles_required('Admin')
def test_principal():
    return render_template('test.html')


@restricted_bp.route('/apfa/agregar_lista', methods=['GET', 'POST'])
@login_required
@roles_required('Admin')
def agregar_lista():
    print('VOY A AGREGAR UNA LISTA')
    form = AgregarListaForm()
    if form.validate_on_submit():
        num_lista = int(form.num_lista.data)
        if not Lista.get_by_num_lista(num_lista):
            presidente = form.presidente.data
            vicepresidente = form.vicepresidente.data
            file = form.imagen.data
            print(f'FILE_TYPE: {type(file)}')
            image_name = None
            if file:
                image_name = secure_filename(file.filename)
                images_dir = current_app.config['POSTS_IMAGES_DIR']
                os.makedirs(images_dir, exist_ok=True)
                file_path = os.path.join(images_dir, image_name)
                file.save(file_path)

                # image = Image.open(file_path)
                # print(f'ORIGINAL SIZE: {image.size}')
                # image.thumbnail((128, 128))
                # image.save(file_path)

            lista = Lista(presidente=presidente, vice=vicepresidente, num_lista=num_lista, imagen=image_name)
            lista.save()
            flash('Lista agregada')
            return redirect(url_for('restricted.agregar_lista'))
        else:
            flash('Número de lista ya en sistema')
    return render_template('agregar_lista.html', form=form)
