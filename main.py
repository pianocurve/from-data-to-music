"""`main` is the top level module for your Bottle application."""

import logging

# import the Bottle framework


from bottle import Bottle, template,debug,view

# Create the Bottle WSGI application.
bottle = Bottle()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
debug(True)

# Define an handler for the root URL of our application.
@bottle.route('/<name>/<count:int>')
@view("hello_template")
def hello(name, count):
    return dict(name=name, count=count)



# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.'
