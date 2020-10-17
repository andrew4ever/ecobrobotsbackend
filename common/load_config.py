from dotenv import load_dotenv


def load_config():
    load_dotenv(dotenv_path='.env', override=True)
