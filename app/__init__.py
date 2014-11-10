#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Application
    ~~~~~~~~~~~

    The Flask application module.

    :author: Jeff Kereakoglow
    :date: 2014-11-09
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Flask, render_template
from werkzeug.contrib.cache import SimpleCache

# Initialize the app and the ORM
app = Flask(__name__)
cache = SimpleCache(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_object("config")

#-- Models
# from app.models import user

#-- Controllers
from app.controllers import public
# from app.controllers import private

app.register_blueprint(public.mod)
# app.register_blueprint(private.mod)

view_args = {"title":"Not found",
            "stylesheet":"error",
            "show_header":False,
            "show_footer":False}

#-- Error handlers
@app.errorhandler(403)
def forbidden(error):
    """
    Renders 403 page

    :returns: HTML
    :rtype: flask.Response
    """

    view_args["title"] = "Forbidden"
    return render_template("403.html", args=view_args), 403

@app.errorhandler(404)
def not_found(error):
    """
    Renders 404 page

    :returns: HTML
    :rtype: flask.Response
    """
    view_args["title"] = "Not found"
    return render_template("404.html", args=view_args), 404

@app.errorhandler(500)
def not_found(error):
    """
    Renders 404 page

    :returns: HTML
    :rtype: flask.Response
    """
    view_args["title"] = "Internal server error"
    return render_template("500.html", args=view_args), 500
