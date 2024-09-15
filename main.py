import os
import sys
import json
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

config = {}


def load_config(file_path):
    global config
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)


@app.route('/api/get_yandex_login_url')
def get_yandex_login_url():
    if 'oauth_client_id_yandex' not in config:
        return jsonify({'error': 'OAuth client ID not configured'}), 500
    yandex_oauth_url = f"https://oauth.yandex.com/authorize?client_id={config['oauth_client_id_yandex']}"
    return jsonify({'url': yandex_oauth_url})


@app.route('/login/authorized')
def login_authorized():
    return jsonify({'message': 'Login authorized'}), 200


@app.route('/<path:filename>')
def serve_static_file(filename):
    static_folder = './static'
    file_path = os.path.join(static_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(static_folder, filename)
    else:
        return send_from_directory(static_folder, '404.html'), 404


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python app.py <config.json>")
        sys.exit(1)
    
    load_config(sys.argv[1])

    port = config.get('port', 5000)
    app.run(host='0.0.0.0', port=port)
