"""This allows Gunicorn to serve the app in production"""

import app

app = app.create_app()
