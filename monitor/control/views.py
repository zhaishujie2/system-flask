from flask import Blueprint, Response, request
import json
from es_demo import es_index, get_number,get_data,get_condition_data,get_condition_number
from system_message import get_all_system,get_node_system

mod = Blueprint('control', __name__, url_prefix='/control')


@mod.route('/test')
def turkey_org():
    return "success"


@mod.route('/get_all')
def turkey_org1():
    result = get_all_system()
    #    resp = Response(result)
    #    resp.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps(result)

@mod.route('/get_node')
def turkey_org2():
    ip = request.args.get('ip', '')
    result = get_node_system(ip)
    #    resp = Response(result)
    #    resp.headers['Access-Control-Allow-Origin'] = '*'
    return json.dumps(result)

@mod.route("/input_list")
def input_dict():
    lis = request.args.get('lis', '')
    if lis != "":
        es_index(lis)


@mod.route("/get_number")
def output_page_number():
    count = 0
    node = request.args.get('node', '')
    if node != "":
        count = int(get_number(node))
    return str(count)

@mod.route("/get_data")
def output_page_data():
    result = None
    node = request.args.get('node', '')
    page_number = request.args.get('page_number', '')
    page_size = request.args.get('page_size', '')
    if node != "" and page_size != "" and page_number != "":
        result = get_data(node,page_number,page_size)
    return json.dumps(result)

@mod.route("/get_condition_data")
def output_condition_data():
    result = None
    node = request.args.get('node', '')
    page_number = request.args.get('page_number', '')
    page_size = request.args.get('page_size', '')
    keys = request.args.get('keys', '')
    if node != "" and page_size != "" and page_number != "" and keys != "":
        result = get_condition_data(node, page_number, page_size, keys)
    return json.dumps(result)


@mod.route("/get_condition_number")
def output_condition_number():
    count = 0
    node = request.args.get('node', '')
    keys = request.args.get('keys', '')
    if node != "" and keys != "":
        count = int(get_condition_number(node,keys))
    return str(count)


