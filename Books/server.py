from flask_app import app
# ...server.py
from flask_app.controllers import books


if __name__ == "__main__":
    app.run(debug=True)