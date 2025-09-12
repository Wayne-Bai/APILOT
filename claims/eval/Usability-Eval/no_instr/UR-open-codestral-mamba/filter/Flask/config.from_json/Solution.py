from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_mapping({
    "SQLALCHEMY_DATABASE_URI": 'sqlite:////path-to-your-database',  # Replace with your database URI
})
db = SQLAlchemy(app)

@app.route('/update-config', methods=['POST'])
def update_config():
    with app.app_context():
        with open('config.json') as f:
            data = json.load(f)
            app.config.from_mapping(data)
            db.session.commit()
        return 'Config updated successfully'

if __name__ == '__main__':
    app.run(debug=True)
