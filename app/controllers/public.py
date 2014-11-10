#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Public controller
    ~~~~~~~~~~~~~~~
    The public controller.

    All public pages of the application ought to be controlled through this
    file.

    :author: Jeff Kereakoglow
    :date: 2014-11-10
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
from flask import Blueprint, render_template, abort
from app.utils import cache_data, fetch_cached_data

mod = Blueprint("public", __name__)

args = {"title":'',
        "stylesheet":'',
        "show_header":True,
        "show_footer":True}

@mod.route('/', methods=["GET"])
def home():
    """
    Renders the view for the home controller.

    :returns: HTML
    :rtype: flask.Response
    """

    args["title"] = "Home"
    args["show_header"] = True
    args["show_footer"] = True

    # Prevent caching if in debug mode.
    # return render_template("public/home.html", args=args)

    # Check for a cached response
    rv = fetch_cached_data()

    if rv is not None:
        return rv

    out = render_template("public/home.html", args=args)

    # Automatically cached for 15 minutes
    cache_data(out)

    return out

@mod.route('/forbidden', methods=["GET"])
def raise_403():
    abort(403)

@mod.route('/not-a-real-url', methods=["GET"])
def raise_404():
    abort(404)

@mod.route('/internal-server-error', methods=["GET"])
def raise_500():
    abort(500)
