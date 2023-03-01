import os
# from dotenv import load_dotenv
# from blog.enums import EnvType
#
# load_dotenv()
#
#
# ENV = os.getenv('FLASK_ENV', default=EnvType.production)
# DEBUG = ENV == EnvType.development
#
# SECRET_KEY = os.getenv('SECRET_KEY')
#
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
# SQLALCHEMY_TRACK_MODIFICATIONS = False


class BaseConfig(object):
    DEBUG = False
    Testing = False
    # SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "abcdefg123456"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
