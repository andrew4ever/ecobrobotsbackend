from dotenv import load_dotenv
from os import environ


def load_config():
    env = environ.get('ENVIRONMENT')

    if env == 'DEVELOPMENT':
        load_dotenv(dotenv_path='.env.dev', override=True)

    else:
        load_dotenv(dotenv_path='.env', override=True)
