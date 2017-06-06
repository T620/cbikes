import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = "\xb2\xc3\xa5$O,FJx\xa3\x14vB(\xc5\xe3\xa3\x1a)\xa4\x81\xf2\x8bK"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
