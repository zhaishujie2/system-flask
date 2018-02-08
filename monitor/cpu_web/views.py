from flask import Blueprint
from es_demo import es_index
from system_message import get_all_system
mod = Blueprint('cpu', __name__, url_prefix='/cpu')




