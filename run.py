from app import app
from common import load_config

load_config()
app.run(host='0.0.0.0', port=8080, debug=True)
