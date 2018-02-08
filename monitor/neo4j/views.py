from flask import Blueprint, Response, request
import json
from neo4jget import getNodeID_RelationshipID,get_all
mod = Blueprint('neo4j', __name__, url_prefix='/neo4j')


@mod.route('/get_data')
def turkey_org():
    result = getNodeID_RelationshipID()
    return json.dumps(result)
@mod.route('/get_data_tables')
def turkey_org1():
    result = get_all()
    return json.dumps(result)
