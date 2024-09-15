import sys
import json

import globals
import models
import api_endpoints
import static_pages

def load_config(file_path):
    global config
    try:
        with open(file_path, 'r') as f:
            globals.config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <config.json>")
        sys.exit(1)
    
    load_config(sys.argv[1])

    with globals.app.app_context():
        globals.db.create_all()

    port = globals.config.get('port', 5000)
    globals.app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()