
from flask import Blueprint
router = Blueprint('routes', __name__)

from .user_controller import *
from .admin_controller import *