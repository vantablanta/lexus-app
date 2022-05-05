class Config:
    """Parent Config"""

class DevConfig(Config):
    """Debug Config"""
    DEBUG = True

class ProdConfig(Config):
    """Production Config"""