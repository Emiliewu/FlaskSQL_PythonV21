from flask_app import app
# ...server.py
from flask_app.controllers import dojos_ninjas


if __name__ == "__main__":
    app.run(debug=True)