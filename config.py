class Config:
    """Parent Config"""
    
class DevConfig(Config):
    """Debug Config"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:admin@localhost/lexus'
    

class ProdConfig(Config):
    """Production Config"""

config_options = {
    'dev': DevConfig,
    'prod': ProdConfig
}