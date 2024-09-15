# YAPI

## How to run

- You need to log into your Yandex ID account and create an application. Here is the guide:

    https://yandex.ru/dev/disk-api/doc/ru/concepts/quickstart#quickstart__oauth

    Then go to `config_example.json` and put your public client id into `oauth_client_id_yandex` field.

- Create a virtual environment and install dependencies:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

- Run server: `$ python main.py my_config.json` , and go to the ip of the server.