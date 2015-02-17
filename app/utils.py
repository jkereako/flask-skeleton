#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Utils
    ~~~~~

    Utility methods.

    I'm including this file in the skeleton because it contains methods I've
    found useful.

    The goal is to keep this file as lean as possible.

    :author: Jeff Kereakoglow
    :date: 2014-11-10
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
import re
import logging
from hashlib import sha224
from datetime import date, datetime
from unicodedata import normalize
from flask import request
from app import app, cache

try:
    compat_chr = unichr # Python 2
except NameError:
    compat_chr = chr

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def logcat(message):
    """
    Helper function which logs messages to the terminal.

    Without this helper, the developer would have to write:

    import logging
    from nesn_api import app

    app.logger.debug(message)

    Whereas, with this helper, it has been reduced to:

    from nesn_api.utils import logcat

    logcat(message)

    Coming from Android development, it is a lot easier to remember
    logcat than it is to remember app.logger.debug

    :param message: The log message
    :type message: str
    """
    app.logger.debug(message)

def query_string_arg_to_bool(arg):
    """
    Converts various string representations of Boolean values to an actual
    Boolean object.

    :param arg: The string to convert
    :type arg: str

    :returns: The estimated Boolean representation
    :rtype: Boolean
    """
    param = request.args.get(arg)

    if param is None:
        return False

    elif param.lower() in ("yes", 'y', "true", "t", "1"):
        return True

    return False

def prepare_query_string(args):
    """
    Creates a simple query string.

    This is an alternative to Requests's parameter feature. Requests
    strips stuff out and coverts everything. This does a simple join,
    preserving everything.

    :param args: The data which is to be prepared
    :type args: dict

    :returns: A formatted query string
    :rtype: string
    """
    return '?' + '&'.join(["%s=%s" % (key, value) for (key, value) in args.items()])

def fetch_cached_data(args=None):
    """
    Retrieves a cache object when given an optional cache key.

    Because most cache keys within this app are URL dependent, the
    code which retrieves the cache has been refactored here to maximize
    consistency.

    :param cache_key: The identifier for the cache object. This must be unique
    :type cache_key: str

    :returns: A dictionary of JSON data
    :rtype: dict
    """
    cache_key = request.base_url

    if args:
        cache_key += args

    cache_key = sha224(cache_key).hexdigest()

    rv = cache.get(cache_key)

    # if rv is not None:
    #     rv = "<!-- served from cache -->" + rv
    return rv

def cache_data(data, args=None, timeout=None):
    """
    Stores data in the application cache using the base URL as the main
    cache key.

    To prevent all URLs from being cached, such as
    /teams/nba?this_is_not_a_real_param=2

    The base URL along with optional arguments are used. This ensures
    that URLS passed with arbitrary query string arguments will not
    break the cache.

    Because most cache keys within this app are URL dependent, the
    code which stores the cache has been refactored here to maximize
    consistency.

    :param data: The data object to cache
    :type data: dict

    :param cache_key: The identifier for the cache object. This must be unique
    :type cache_key: str

    :param timeout: The expiry for the cache
    :type timeout: int

    :returns: None
    :rtype: None
    """
    cache_key = request.base_url

    if args:
        cache_key += args

    cache_key = sha224(cache_key).hexdigest()

    timeout = app.config["CACHE_TIMEOUT"] if timeout is None else timeout

    cache.set(cache_key, data, timeout)

#
def slugify(text, delimiter=u'-'):
    """
    Generates an slightly worse ASCII-only slug.

    :see http://flask.pocoo.org/snippets/5/
    :returns: A URL slug
    :rtype: str
    """
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize("NFKD",word).encode("ascii", "ignore")
        if word:
            result.append(word)
    return unicode(delimiter.join(result))

def current_time():
    """
    Returns a UNIX timestamp for the current time.

    :returns: The current timestamp as a string
    :rtype: str
    """
    return datetime.now().strftime("%s")
