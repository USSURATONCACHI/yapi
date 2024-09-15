from flask import send_from_directory
from globals import app, db, config

import os

@app.route('/me')
def me():
    return serve_static_file('me.html')

@app.route('/login/authorized')
def login_authorized():
    return serve_static_file('authorized.html')


@app.route('/')
def index():
    return serve_static_file('index.html')

# All other endpoints should go to folder ./static
@app.route('/<path:filename>')
def serve_static_file(filename):
    static_folder = './static'
    file_path = os.path.join(static_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(static_folder, filename)
    else:
        return send_from_directory(static_folder, '404.html'), 404
