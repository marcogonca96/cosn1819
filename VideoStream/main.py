#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import print_function

import datetime
import logging

# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop

import os
import re
import mimetypes
import sys
import time
import pprint
import sqlite3

from flask import Flask, render_template, Response, request, g, flash, redirect, url_for, send_from_directory, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'videos/'

logger = logging.getLogger(__name__)
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)

MB = 1 << 20
BUFF_SIZE = 10 * MB

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Headers',
  'Access-Control-Allow-Headers, Origin, Accept, X-Access-Token, jwt, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization, username, Cache-Control, Pragma')
  response.headers.add('Cache-Control', 'no-cache')
  response.headers.add('Pragma', 'no-cache')
  return response

def find_videoname(catalogue_id):
    
    connection = sqlite3.connect('instance/videos.sqlite')
    cursor = connection.cursor()    

    query = "SELECT path FROM videos WHERE catalogue_id=?"
    result = cursor.execute(query, (catalogue_id,))
    row = result.fetchone()
    result = ''.join(row)
    return result.encode('ascii','ignore')

@app.route('/videos/<id>', methods = ['GET'])
def home(id):
    response = render_template(
        'index.html',
        video='/api/'+id,
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
   
@app.route('/api/<id>')
def video(id):
    path = find_videoname(id)
    start, end = get_range(request)
    return partial_response(path, start, end)

@app.route('/add_video', methods=['POST'])
def add_video():

    connection = sqlite3.connect('instance/videos.sqlite')
    cursor = connection.cursor()    

    catalogue_id = request.form.get('catalogue_id')
    path = request.form.get('path')
    
    query = "INSERT INTO videos (catalogue_id, path) VALUES (?,?)"
    result = cursor.execute(query, (catalogue_id, path))

    connection.commit()

    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200), 200

@app.route('/upload_video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
    return render_template("upload.html")

if __name__ == '__main__':
    HOST = '0.0.0.0'
    app.run(host=HOST, port=8005, debug=True)
