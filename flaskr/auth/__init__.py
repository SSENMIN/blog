from flask import Blueprint

bp = Blueprint('auth', __name__)

from flaskr.auth import routes