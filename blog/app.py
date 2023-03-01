from flask import Flask
from blog.models.database import db
from blog.views.articles import articles
from blog.views.auth import auth, login_manager
from blog.views.index import index
from blog.views.users import user
import os
from flask_migrate import Migrate


migrate = Migrate()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['DEBUG'] = True
    register_blueprints(app)
    # app.config.from_object('blog.configs')
    cfg_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    db.init_app(app)
    # app.config["SECRET_KEY"] = "abcdefg123456"
    login_manager.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(index)
    app.register_blueprint(articles)
    app.register_blueprint(auth)


# app = Flask(__name__)
#
#
# app.register_blueprint(user)
# app.register_blueprint(index)
# app.register_blueprint(articles)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/blog.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# db.init_app(app)
#
#
# @app.route('/')
# def index():
#     return "<h1>Главная страничка</h1>"
#
#
# @app.route('/greet/<name>/')
# def greet(name: str):
#     return f'Hello {name}'
#
#
# @app.route('/user/')
# def read_user():
#     name = request.args.get('name')
#     surname = request.args.get('surname')
#     return f"User {name or '[no name]'} {surname or '[no surname]'}"
#
#
# @app.route('/status/', methods=['GET', 'POST'])
# def castom_status_code():
#     if request.method == 'POST':
#         return """\
#     To get response with custom status code
#     send request using POST method
#     and pass `code` in JSON body / FormData
#         """
#     print("raw bytes data:", request.data)
#
#     if request.form and 'code' in request.form:
#         return "code from Form", request.form['code']
#
#     if request.json and 'json' in request.json:
#         return "code from json", request.json['code']
#
#     return "", 20
#
#
# @app.before_request
# def process_before_request():
#     g.start_time = time()
#
#
# @app.after_request
# def process_after_request(response):
#     if hasattr(g, "start_time"):
#         response.headers["process-time"] = time() - g.start_time
#
#     return response
#
#
# @app.route("/power/")
# def power_value():
#     x = request.args.get("x") or ""
#     y = request.args.get("y") or ""
#     if not (x.isdigit() and y.isdigit()):
#         app.logger.info("invalid values for power: x=%r and y=%r", x, y)
#         raise BadRequest("please pass integers in `x` and `y` query params")
#
#     x = int(x)
#     y = int(y)
#     result = x ** y
#     app.logger.debug("%s ** %s = %s", x, y, result)
#     return str(result)
#
#
# @app.route("/divide-by-zero/")
# def do_zero_division():
#     return 1 / 0
#
#
# @app.errorhandler(ZeroDivisionError)
# def handle_zero_division_error(error):
#     print(error) # prints str version of error: 'division by zero'
#     app.logger.exception("Here's traceback for zero division error")
#     return "Never divide by zero!", 400
