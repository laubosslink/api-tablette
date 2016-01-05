#!/usr/bin/python
import sys
import subprocess

from optparse import OptionParser

import logging

import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def dessin_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/image', methods=['POST'])
def dessin_upload_file():
    file = request.files['file']
    if file and dessin_allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))
        return ('', 204)

@app.route('/image/<filename>', methods=['POST', 'GET']) # TODO replace filename by id from database
def dessin_edit_get_file(filename):
    if request.method == 'POST': # edit
        file = request.files['data']
        if file and dessin_allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))
            return ('', 204)

    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/image/delete/<filename>', methods=['GET'])
def dessin_delete_file(filename):
    try:
        os.remove(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))
    except Exception as e:
        return (str(e), 202)
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
