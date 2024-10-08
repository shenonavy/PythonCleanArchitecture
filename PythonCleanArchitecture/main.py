# """
# This script runs the application using a development server.
# It contains the definition of routes and views for the application.
# """

from flask import Flask
from app.controllers import router
app = Flask(__name__)

# # Make the WSGI interface available at the top level so wfastcgi can get it.
# wsgi_app = app.wsgi_app

app.register_blueprint(router)


@app.route('/')
def hello():
    """Renders a sample page."""
    return "---------------Api is running---------------"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5001'))
    except ValueError:
        PORT = 5001
    app.run(HOST, PORT)
