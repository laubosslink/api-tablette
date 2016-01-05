#!/usr/bin/python
import sys
import subprocess

from optparse import OptionParser

import logging

import os
from flask import Flask, request, redirect, url_for, send_from_directory, json
from werkzeug import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# DESSINS

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

# INFOS

@app.route('/info', methods=["POST"])
def info_create():
    title = request.title
    content = request.content

@app.route('/info/<id>', methods=["GET"])
def info_get(id):
    return json.jsonify(title="title from DB", content="content from DB")

@app.route('/info/delete/<id>', methods=['GET'])
def info_delete(id):
    return ('', 204)

# FORUM
@app.route('/post/', methods=['POST'])
def post_create():
    title = request.title
    content = request.content
    picture = request.picture

@app.route('/post/<id>', methods=["GET"])
def post_get(id):
    return json.jsonify(posts="return posts with comments, and vote")

@app.route('/post/<id>/vote/<vote_value>', methods=['POST'])
def post_vote(id, vote_value):
    return ('', 204)

@app.route('/post/delete/<id>', methods=['GET'])
def post_delete(id):
    return ('', 204)

@app.route('/post/<post_id>/comment', methods=['POST'])
def comment_create(post_id):
    content = request.content

@app.route('/post/<post_id>/comment/<id>', methods=["GET"])
def comment_get(post_id, id):
    return json.jsonify(posts="return posts with comments, and vote")

@app.route('/post/<post_id>/comment/<id>/vote/<vote_value>', methods=['POST'])
def comment_vote(post_id, id, vote_value):
    return ('', 204)

@app.route('/post/<post_id>/comment/delete/<id>', methods=['GET'])
def comment_delete(post_id, id):
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
