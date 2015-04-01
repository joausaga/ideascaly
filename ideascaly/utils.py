# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

import six
import dateutil.parser


def parse_datetime(str_date):
    try:
        date_is = dateutil.parser.parse(str_date)
        return date_is
    except:
        return None

def parse_html_value(html):
    return html[html.find('>')+1:html.rfind('<')]


def parse_a_href(atag):
    start = atag.find('"') + 1
    end = atag.find('"', start)
    return atag[start:end]


def convert_to_utf8_str(arg):
    # written by Michael Norton (http://docondev.blogspot.com/)
    if isinstance(arg, six.text_type):
        arg = arg.encode('utf-8')
    elif not isinstance(arg, bytes):
        arg = six.text_type(arg).encode('utf-8')
    return arg


def import_simplejson():
    try:
        import simplejson as json
    except ImportError:
        try:
            import json  # Python 2.6+
        except ImportError:
            raise ImportError("Can't load a json library")

    return json