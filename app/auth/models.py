from app import db
# from flask_login import UserMixin
from flask_user import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    habilitado = db.Column(db.Boolean, default=False)
    ya_voto = db.Column(db.Boolean, default=False)
    # TODO: Hacer roles
    email_confirmed_at = db.Column(db.DateTime())
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    numero_socio = db.Column(db.Integer, db.ForeignKey('padron.num_padron', ondelete='CASCADE'))
    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'<User: {self.nombre} - Email: {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def confirmar_voto(self):
        self.ya_voto = True
        db.session.commit()

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_num_socio(num_socio):
        return User.query.filter_by(numero_socio=num_socio).first()

    # @staticmethod
    # def get_user_by_token(token):
    #     return User.query.get(int(token))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<Role: {self.name}>'

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

    def __repr__(self):
        return f'<User: {self.user_id} - Role: {self.role_id}'