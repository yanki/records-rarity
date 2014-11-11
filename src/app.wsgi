import os

# local environment
os.chdir(os.path.dirname(__file__))

import bottle

# Routes are handled in the routes.py file
import routes

# Disable debug mode
bottle.debug(False)

application = bottle.default_app()
