import requests

from flask import request, jsonify, send_from_directory
from datetime import datetime, timedelta

from models import User, OAuthToken
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

    if not (has_token and has_expiration):
        return jsonify({'error': 'Incorrect arguments'}), 401
    
    token = data.get('access_token')
    expires_in = int(data.get('expires_in'))

    print("Testing token validity")
    print(token)
    print(expires_in)

    url = 'https://login.yandex.ru/info?format=json'
    headers = {
        'Authorization': f'OAuth {token}'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Process the response from Yandex
            data = response.json()
            print('Successfully queried data')
            client_id = data['client_id']
            first_name = data['first_name']
            expires_at = datetime.utcnow() + timedelta(seconds=expires_in)

            check_token = OAuthToken.query.filter_by(token=token).first()
            if check_token:
                return jsonify({
                    'redirect_to': '/me',
                    'current_access_token': token
                }), 200
            
            check_user = User.query.filter_by(id=client_id).first()
            if not check_user:
                print('User does not exist')
                new_user = User(id=client_id, name=first_name)
                new_token = OAuthToken(token=token, user_id=new_user.id, expires_at=expires_at)

                new_user.auth_tokens.append(new_token)

                globals.db.session.add(new_user)
                globals.db.session.commit()
                print('Created such user')
            else:
                added_token = OAuthToken(token=token, user_id=check_user.id, expires_at=expires_at)
                check_user.auth_tokens.append(added_token)
                globals.db.session.add(added_token)
                globals.db.session.commit()
                print('Added an OAuth token to the user')

            return jsonify({
                'redirect_to': '/me',
                'current_access_token': token
            }), 200
        else:
            print('Code is not 200: ', response.status_code)
            return jsonify({"message": "Invalid token"}), 401

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print('Exception happened: ', e)
        return jsonify({"error": str(e)}), 500



@globals.app.route('/api/am_i_logged_in')
def am_i_logged_in():
    token = request.headers.get('Authorization')

    if token:
        print(token)
        print("Testing token validity")

        url = 'https://login.yandex.ru/info?format=json'
        headers = {
            'Authorization': f'OAuth {token}'
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Process the response from Yandex
                data = response.json()
                print('Successfully queried data')
                print(data)

                return jsonify({"message": "Yes"}), 200
            else:
                print('Code is not 200: ', response.status_code)
                return jsonify({"message": "Invalid token"}), 401

        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the request
            print('Exception happened: ', e)
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"message": "No Authorization token provided"}), 401