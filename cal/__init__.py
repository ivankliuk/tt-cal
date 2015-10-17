"""Main entry point
"""
from pyramid.config import Configurator

from cal.db.tools import load_defaults


def main(global_config, **settings):

    # Since SQLAlchemy uses SQLite which stores its data into memory,
    # initial data should be loaded every time the application starts.
    load_defaults()

    config = Configurator(settings=settings)
    config.include("cornice")
    config.include('pyramid_mako')
    config.scan("cal.views")

    # Add static for serving front-end of the application
    config.add_static_view(name='/static', path='static')

    return config.make_wsgi_app()
