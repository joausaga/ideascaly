# IdeaScaly
# Copyright 2015 Jorge Saldivar
# See LICENSE for details.

import datetime
import mimetypes
import os
import six


from ideascaly.error import IdeaScalyError


def parse_datetime(long_ms):
    try:
        date_is = datetime.datetime.fromtimestamp(long_ms/1e3)
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
    elif isinstance(arg, bytes):
        arg = arg.decode('utf-8')
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


def pack_image(filename, max_size, form_field='image'):
        """Pack an image from file into multipart-formdata post body"""
        try:
            if os.path.getsize(filename) > (max_size * 1024):
                raise IdeaScalyError('File is too big, must be less than %skb.' % max_size)
        except os.error as e:
            raise IdeaScalyError('Unable to access file: %s' % e.strerror)

        # build the mulitpart-formdata body
        fp = open(filename, 'rb')

        # image must be gif, jpeg, or png
        file_type = mimetypes.guess_type(filename)
        if file_type is None:
            raise IdeaScalyError('Could not determine file type')
        file_type = file_type[0]
        if file_type not in ['image/gif', 'image/jpeg', 'image/png']:
            raise IdeaScalyError('Invalid file type for image: %s' % file_type)

        if isinstance(filename, six.text_type):
            filename = filename.encode('utf-8')

        BOUNDARY = b'Id34Sc4ly'
        body = list()
        body.append(b'--' + BOUNDARY)
        body.append('content-disposition: form-data; name="{0}";'
                    ' filename="{1}"'.format(form_field, filename)
                    .encode('utf-8'))
        body.append('content-type: {0}'.format(file_type).encode('utf-8'))
        body.append(b'')
        body.append(fp.read())
        body.append(b'--' + BOUNDARY + b'--')
        body.append(b'')
        fp.close()
        body = b'\r\n'.join(body)
        body_length = str(len(body))

        # build headers
        headers = {
            'content-type': 'multipart/form-data; boundary={0}'.format(BOUNDARY),
            'content-length': body_length
        }

        return headers, body