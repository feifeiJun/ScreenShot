import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = '83010e3753f0114bd1539bd6bd72d9f4fc6c791d0ac3581c654552899b2f226d'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    DEBUG_TB_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = '83010e3753f0114bd1539bd6bd72d9f4fc6c791d0ac3581c654552899b2f226d'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
    DEBUG_TB_ENABLED = False