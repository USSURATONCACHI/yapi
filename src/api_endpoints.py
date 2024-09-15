from flask import request, jsonify, send_from_directory

import globals

@globals.app.route('/api/get_yandex_login_url')
def get_yandex_login_url():
    if 'oauth_client_id_yandex' not in globals.config:
        return jsonify({'error': 'OAuth client ID not configured'}), 500

    yandex_oauth_url = f"https://oauth.yandex.com/authorize?response_type=token&client_id={globals.config['oauth_client_id_yandex']}"
    
    return jsonify({'url': yandex_oauth_url})

@globals.app.route('/api/yandex_authorize', methods=['POST'])
def yandex_authorize():
    data = request.get_json()

    has_token = 'access_token' in data and data['access_token']
    has_expiration = 'expires_in' in data and data['expires_in']

    if has_token and has_expiration:
        print(data.get('access_token'))
        print(data.get('expires_in'))

        return jsonify({
            'redirect_to': '/me',
            'current_access_token': 'sigma-0001'
        })
    else:
        return jsonify({'error': 'Incorrect arguments'}), 



@globals.app.route('/api/am_i_logged_in')
def am_i_logged_in():
    token = request.headers.get('Authorization')

    if token:
        print(token)
        return jsonify({"message": "Yes"}), 200

    return jsonify({"message": "No"}), 401