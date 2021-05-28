import dj_database_url
from decouple import config


class DB:
    @classmethod
    def config(cls, debug):
        return cls.development() if debug else cls.production()

    @classmethod
    def production(cls):
        return {
            'default': {
                **dj_database_url.parse(config('DATABASE_URL')),
                'ENGINE': 'django.db.backends.postgresql'
            }
        }

    @classmethod
    def development(cls):
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'devsprimedb',
                'HOST': 'db',
                'USER': config('DBUSER', default='postgres'),
                'PASSWORD': config('DBPASSWD', default='postgres'),
            }
        }
