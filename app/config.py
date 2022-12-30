import os

# configuraciones. True para que el servidor pueda ser levantado en modo debug
DEBUG = True

# configuracion BD
SECRET_KEY =  'A SECRET KEY'
SECURITY_PASSWORD_SALT = 'my_precious_two'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = 'sqlite:///apfa.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///d:\\Users\\f108119\\Downloads\\Proyectos\\Python\\APFA\\app\\apfa.db'

USER_REGISTER_URL = '/apfa/register'
USER_LOGIN_URL = '/apfa/login'
USER_UNAUTHENTICATED_ENDPOINT = 'auth.login'
USER_UNAUTHORIZED_ENDPOINT = 'auth.login'
USER_ENABLE_EMAIL = False

# configuracion mail
MAIL_SERVER = 'smtp-mail.outlook.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = True
# gmail authentication
MAIL_USERNAME = 'pruebasdemaxi@outlook.com'
MAIL_PASSWORD = '#PruebaS2022'
MAIL_SUBJECT = "Por favor, confirme su registro."
# mail accounts
MAIL_DEFAULT_SENDER = 'pruebasdemaxi@outlook.com'

# directorio para guardar imagenes
POSTS_IMAGES_DIR = 'app\static\images'
