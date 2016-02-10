# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2016 Jonathan Labéjof <jonathan.labejof@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------

"""Module dedicated to ease registration and instanciation of middleware from
an URL.
"""

__all__ = ['URLMiddleware', 'fromurl']

from six.moves.urllib.parse import urlparse

from .core import get
from .cls import Middleware


class URLMiddleware(Middleware):
    """Middleware instanciated with a URL properties."""

    DEFAULT_HOST = 'localhost'  #: default host.

    def __init__(
            self, scheme, host=DEFAULT_HOST, port=None, user=None, pwd=None,
            path='', query='', params='', fragment='',
            *args, **kwargs
    ):
        """
        :param str scheme: url scheme which corresponds to one of this protocl.
        :param str host: host name.
        :param int port: port value.
        :param str user: user name.
        :param str pwd: user password.
        :param str path: url path.
        :param str query: url query.
        :param
        """

        super(URLMiddleware, self).__init__(*args, **kwargs)

        self.scheme = scheme
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.path = path
        self.query = query
        self.params = params
        self.fragment = fragment


def fromurl(url):
    """Get a middleware from an URL.

    The middleware is choosen from the scheme and might accept such as callable
    parameters:

    - a scheme: registered protocol.
    - an host: url hostname.
    - a port: url port.
    - an username: user name.
    - a password: a password value.
    - a path: url path.
    - a query: url query.
    - params: url params.
    - fragment: fragment.

    :return: middleware initialized with url properties.
    """

    parseduri = urlparse(url)

    protocol = parseduri.scheme

    middleware = get(protocol)

    result = middleware(
        host=parseduri.hostname, port=parseduri.port,
        user=parseduri.username, pwd=parseduri.password,
        path=parseduri.path, query=parseduri.query, params=parseduri.params,
        fragment=parseduri.fragment
    )

    return result
