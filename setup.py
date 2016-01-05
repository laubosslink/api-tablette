#!/usr/bin/python
import sys
import subprocess

from optparse import OptionParser

import logging

from flask import Flask

app = Flask(__name__)

import os
from flask import Blueprint, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

route_upload_file = Blueprint('upload_file', __name__)
route_uploaded_file = Blueprint('uploaded_file', __name__)

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER + "/dessins/", filename))
            return url_for('uploaded_file', filename=filename)

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type="file" name="file">
         <input type="submit" value="Upload">
    </form>
    '''

@app.route('/image/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
