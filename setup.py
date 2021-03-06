#!/usr/bin/python
import sys
import subprocess

from optparse import OptionParser

import logging

import os
from flask import Flask, request, redirect, url_for, send_from_directory, json
from werkzeug import secure_filename

from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker

from scripts.create_db import Info, Drawing


engine = create_engine('sqlite:///db.sql')

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

# DESSINS

def dessin_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/image', methods=['POST', 'GET'])
@crossdomain(origin='*')
def dessin_upload_file():
    if request.method == 'POST':
        title = request.form.get('title')
        file = request.files['file']

        if file and dessin_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))

            draw = Drawing(title, filename)

            try:
                session.add(draw)
                session.commit()
            except Exception as e:
                session.rollback()
                logging.error('L\'image existe deja : ' + str(e))

            return (str(draw.id), 202)


    images = session.query(Drawing).all()

    ids = []

    for image in images:
        ids.append(image.id)

    return json.dumps(ids)

@app.route('/image/main', methods=['GET'])
@crossdomain(origin='*')
def dessin_image_principale():
    draw = session.query(Drawing).filter(Drawing.main == 1).all()[0]
    return send_from_directory(app.config['UPLOAD_FOLDER'] + '/dessins/', draw.filename)

@app.route('/image/<draw_id>', methods=['POST', 'GET'])
@crossdomain(origin='*')
def dessin_edit_get_file(draw_id):

    draw = session.query(Drawing).get(draw_id)

    if request.method == 'POST': # edit
        file = request.files['file']
        if file and dessin_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))
            # TODO update date modification
            return ('', 204)

    return send_from_directory(app.config['UPLOAD_FOLDER'] + '/dessins/', draw.filename)

@app.route('/image/title/<title>', methods=['GET'])
@crossdomain(origin='*')
def dessin_get_file_by_title(title):
    draw = session.query(Drawing).filter(Drawing.title == title).all()[0]
    return send_from_directory(app.config['UPLOAD_FOLDER'], draw.filename)

@app.route('/image/delete/<draw_id>', methods=['GET'])
@crossdomain(origin='*')
def dessin_delete_file(draw_id):

    file = session.query(Drawing).get(draw_id)

    try:
        os.remove(os.path.join(UPLOAD_FOLDER + "/dessins/", file.filename))
    except Exception as e:
        return (str(e), 202)

    try:
        session.delete(file)
        session.commit()
    except:
        logging.error('Cannot delete file in database')

    return ('', 204)

# INFOS
@app.route('/info', methods=['POST', 'GET'])
@crossdomain(origin='*')
def info_create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        info = Info(title, content)

        try:
            session.add(info)
            session.commit()
        except Exception as e:
            session.rollback()
            logging.error('L\'information existe deja : ' + str(e))

        return (str(info.id), 202)

    infos = session.query(Info).all()

    ids = []

    for info in infos:
        ids.append(info.id)

    return json.dumps(ids)

@app.route('/info/<id>', methods=['GET'])
@crossdomain(origin='*')
def info_get(id):
    info = session.query(Info).get(id)
    return json.jsonify(title=info.title, content=info.content)


@app.route('/info/main', methods=['GET'])
@crossdomain(origin='*')
def info_get_principale():
    info = session.query(Info).filter(Info.main == 1).all()[0]
    return (info.content, 202)

@app.route('/info/title/<title>', methods=['GET'])
@crossdomain(origin='*')
def info_get_by_title(title):
    info = session.query(Info).filter(Info.title == title).all()[0]
    return (info.content, 202)

@app.route('/info/delete/<info_id>', methods=['GET'])
@crossdomain(origin='*')
def info_delete(info_id):
    session.query(Info).filter_by(id=info_id).delete()
    return ('', 204)

if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option('-t', '--tests', action='store_true', help='Allow to run all tests', default=False)
    parser.add_option('-d', '--debug', type='string', help='Available levels are CRITICAL (3), ERROR (2), WARNING (1), INFO (0), DEBUG (-1)', default='ERROR')
    options, args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, options.debug))

    if options.debug == logging.DEBUG:
        app.config['PROPAGATE_EXCEPTIONS'] = True
        app.debug = True
    elif options.tests:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
        sys.exit(0)

    logging.debug('Running flask')

    app.run()
