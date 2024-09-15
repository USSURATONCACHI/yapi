import sys
import json

from globals import app, db, config
import models
import api_endpoints
import static_pages

def load_config(file_path):
    global config
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

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