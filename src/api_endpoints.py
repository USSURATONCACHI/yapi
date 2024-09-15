from flask import request, jsonify, send_from_directory

from globals import app, db, config

@app.route('/api/get_yandex_login_url')
def get_yandex_login_url():
    if 'oauth_client_id_yandex' not in config:
        return jsonify({'error': 'OAuth client ID not configured'}), 500
    yandex_oauth_url = f"https://oauth.yandex.com/authorize?response_type=token&client_id={config['oauth_client_id_yandex']}"
    return jsonify({'url': yandex_oauth_url})

@app.route('/api/yandex_authorize', methods=['POST'])
def yandex_authorize():
    data = request.get_json()

    print(data.get('access_token'))
    print(data.get('expires_in'))

    return jsonify({
        'redirect_to': '/me',
        'current_access_token': 'sigma-0001'
    })