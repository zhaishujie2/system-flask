# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import *
from monitor.control.views import mod as controlModule
from monitor.neo4j.views import mod as neo4jModule


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    CORS(app, supports_credentials=True)
    # Create modules
    app.register_blueprint(controlModule)
    app.register_blueprint(neo4jModule)
    # Enable the toolbar?
    app.config['DEBUG_TB_ENABLED'] = app.debug
    # Should intercept redirects?
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
    # Enable the profiler on all requests, default to false
    app.config['DEBUG_TB_PROFILER_ENABLED'] = True
    # Enable the template editor, default to false
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    # debug toolbar
    # toolbar = DebugToolbarExtension(app)

    # the debug toolbar is only enabled in debug mode
    app.config['DEBUG'] = True

    app.config['ADMINS'] = frozenset(['17789624306@163.com'])
    app.config['SECRET_KEY'] = 'SecretKeyForSessionSigning'
    app.config['THREADS_PER_PAGE'] = 8

    app.config['CSRF_ENABLED'] = True
    app.config['CSRF_SESSION_KEY'] = 'somethingimpossibletoguess'

    app.config["MONGO_DBNAME"] = "news"
    app.config["MONGO_HOST"] = "219.224.134.227"
    app.config["MONGO_PORT"] = 99999

    # mongo.init_app(app)

    return app
