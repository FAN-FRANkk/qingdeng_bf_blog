from flask import Flask

app = Flask(__name__)

from start import users_blueprint

app.register_blueprint(blueprint=users_blueprint, url_prefix='/start')

if __name__ == '__main__':
    app.run(debug=True)