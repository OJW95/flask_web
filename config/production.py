from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'web.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'ctm \xd7h\xb0\xc4\x06C\xb4\\\x82]\x14)'