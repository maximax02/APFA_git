from app import db

class Padron(db.Model):
    __tablename__ = 'padron'

    id = db.Column(db.Integer, primary_key=True)
    num_padron = db.Column(db.Integer, unique=True, nullable=False)

    usuarios = db.relationship('User', backref='padron', lazy='dynamic')

class Lista(db.Model):
    __tablename__ = 'lista'

    id = db.Column(db.Integer, primary_key=True)
    presidente = db.Column(db.String(80), nullable=False)
    vice = db.Column(db.String(80), nullable=False)
    num_lista = db.Column(db.Integer, nullable=False, unique=True)
    cantidad_votos = db.Column(db.Integer, default='0')

    # TODO: Poner imagen
    imagen = db.Column(db.String(70), nullable=True, default="")
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    def sumar_voto(self):
        self.cantidad_votos += 1
        db.session.commit()

    @staticmethod
    def get_by_num_lista(num_lista):
        return Lista.query.filter_by(num_lista=num_lista).first()

class Modal():
    def __init__(self, nombre, cancelBtn, continueBtn, link):
        self.nombre = nombre
        self.cancelBtn = cancelBtn
        self.continueBtn = continueBtn
        self.link = link

