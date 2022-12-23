import re

from app.auth.models import User, Role, UserRoles
from app.public.models import Padron, Lista

from app import create_app, db
app = create_app()

with app.app_context():
    db.session.commit()

    db.drop_all()
    db.create_all()

    db.session.commit()



    # Carga de datos del padron
    archivo = open("padron.html", "r", encoding="utf8")
    padron = archivo.read()
    pattern = re.compile("</span>(\d\d\d)</div>")
    matching = pattern.findall(padron)
    nros_socio = []
    for n in matching:
        nros_socio.append(n)
        db.session.add(Padron(num_padron=int(n)))
    print(nros_socio)

    # Cargo un usuario
    user1 = User(nombre="Maxi", apellido="Piñeyro", email="coso@coso.com", numero_socio="614", habilitado=True)
    user1.set_password("123")
    db.session.add(user1)

    # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
    user = User(nombre="Admin", apellido="admin", email="admin@example.com", is_admin=True, habilitado=True)
    user.set_password("blabla")
    user.roles.append(Role(name='Admin'))
    user.roles.append(Role(name='Agent'))
    db.session.add(user)
    db.session.commit()



    # Creo listas
    l1 = Lista(presidente="Anulado", vice="Anulado", num_lista="0", imagen="anulado.jpg")
    l2 = Lista(presidente="Blanco", vice="Blanco", num_lista="1", imagen="blanco.jpg")
    l3 = Lista(presidente="Erica Zorrilla", vice="Consuelo Escudero", num_lista="150", imagen="150.jpg")
    l4 = Lista(presidente="Manuel Agustín Ledesma", vice="Silvia Stipcich ", num_lista="300", imagen="300.jpg")
    l5 = Lista(presidente="Gustavo Gabriel Diaz", vice="Julio Cesar Banchero", num_lista="222", imagen="222.jpg")

    db.session.add(l1)
    db.session.add(l2)
    db.session.add(l3)
    db.session.add(l4)
    db.session.add(l5)

    db.session.commit()

    l1.sumar_voto()