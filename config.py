#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Config
    ~~~~~~

    Application-wide configurations.

    You can put whatever you want here. The convention is to write configuration
    variables in upper-case.

    :see http://flask.pocoo.org/docs/config/

    :author: Jeff Kereakoglow
    :date: 2014-11-10
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = "development_key"
CACHE_TIMEOUT = 60 * 60 * 15
APP_NAME = "Flask Skeleton"
