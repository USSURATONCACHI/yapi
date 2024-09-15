import os
import sys
import json

from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from globals import app, db, config
import models

def load_config(file_path):
    global config
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)


# API endpoints
@app.route('/api/get_yandex_login_url')
def get_yandex_login_url():
    if 'oauth_client_id_yandex' not in config:
        return jsonify({'error': 'OAuth client ID not configured'}), 500
    yandex_oauth_url = f"https://oauth.yandex.com/authorize?response_type=token&client_id={config['oauth_client_id_yandex']}"
    return jsonify({'url': yandex_oauth_url})

@app.route('/api/yandex_authorize', methods=['POST'])
def yandex_authorize():
    print(request.get_json())

    return jsonify({'msg': 'Hello, world!'})


# Static pages
@app.route('/login/authorized')
def login_authorized():
    return serve_static_file('authorized.html')


@app.route('/')
def index():
    return serve_static_file('index.html')


@app.route('/<path:filename>')
def serve_static_file(filename):
    static_folder = './static'
    file_path = os.path.join(static_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(static_folder, filename)
    else:
        return send_from_directory(static_folder, '404.html'), 404
        
def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <config.json>")
        sys.exit(1)
    
    load_config(sys.argv[1])

    with app.app_context():
        db.create_all()

    port = config.get('port', 5000)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()