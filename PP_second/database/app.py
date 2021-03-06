from flask import Flask 
from sqlalchemy.orm.exc import NoResultFound
from flask_httpauth import HTTPBasicAuth
from blueprint import api_blueprint
from error_handlers import not_found, server_error

DEBUG = True
app = Flask(__name__)

app.register_blueprint(api_blueprint, url_prefix="/api/articles")

app.register_error_handler(NoResultFound, not_found)
app.register_error_handler(Exception, server_error)
auth = HTTPBasicAuth()
#app.register_error_handler(Exception, db_error)



if __name__ == '__main__':
    app.run(debug=True)
