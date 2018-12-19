from __future__ import print_function

import datetime
import logging

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import os
import re
import mimetypes
import sys
import time
import pprint
import sqlite3

from flask import Flask, render_template, Response
from flask import request
from frask import g 

DATABASE = '/instance/videos.sqlite'

logger = logging.getLogger(__name__)
app = Flask(__name__)

VIDEO_PATH = '/videos'

MB = 1 << 20
BUFF_SIZE = 10 * MB


@app.route('/')
def home():
    logger.info('Rendering home page')
    response = render_template(
        'index.html',
        time=str(datetime.datetime.now()),
        video=VIDEO_PATH,
    )
    return response


def partial_response(path, start, end=None):
    logger.info('Requested: %s, %s', start, end)
    file_size = os.path.getsize(path)

    # Determine (end, length)
    if end is None:
        end = start + BUFF_SIZE - 1
    end = min(end, file_size - 1)
    end = min(end, start + BUFF_SIZE - 1)
    length = end - start + 1

    # Read file
    with open(path, 'rb') as fd:
        fd.seek(start)
        bytes = fd.read(length)
    assert len(bytes) == length

    response = Response(
        bytes,
        206,
        mimetype=mimetypes.guess_type(path)[0],
        direct_passthrough=True,
    )
    response.headers.add(
        'Content-Range', 'bytes {0}-{1}/{2}'.format(
            start, end, file_size,
        ),
    )
    response.headers.add(
        'Accept-Ranges', 'bytes'
    )
    logger.info('Response: %s', response)
    logger.info('Response: %s', response.headers)
    return response


def get_range(request):
    range = request.headers.get('Range')
    logger.info('Requested: %s', range)
    m = re.match('bytes=(?P<start>\d+)-(?P<end>\d+)?', range)
    if m:
        start = m.group('start')
        end = m.group('end')
        start = int(start)
        if end is not None:
            end = int(end)
        return start, end
    else:
        return 0, None


@app.route(VIDEO_PATH)
def video():
    path = 'videos/lionKingTrailer'
    start, end = get_range(request)
    return partial_response(path, start, end)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print("Starting")
    HOST = '0.0.0.0'
    #http_server = HTTPServer(WSGIContainer(app))
    #http_server.listen(8080)
    #IOLoop.instance().start()
    print("Running")

    # Standalone
    app.run(host=HOST, port=8080, debug=True)
