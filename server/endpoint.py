"""
    This module contains all valid server endpoints.
"""
from flask import Blueprint, request, jsonify
from .handlers import new_agent, existing_agent
ROUTES = Blueprint('endpoint', __name__)

@ROUTES.route('/', methods=['POST'])
def handle_agent():
    """
    This method handles any incoming agent connections.
    """
    data = request.get_json()
    # TODO: Add log

    session_id = data.get('session_id')

    resp = {
        'error': True
    }
    if not session_id:
        resp = new_agent(data)
    else:
        resp = existing_agent(data)

    json_resp = jsonify(resp)
    json_resp.headers['Connection'] = 'close'

    return json_resp

@ROUTES.route('/test')
def test_response():
    """
    This function will return a sample of a standard response using static data.
    """
    resp = jsonify({
        "session_id": "Your Session ID",
        "actions": [
            {
                "action_id": "some action ID to track",
                "command": "echo",
                "args": ["hi dad"],
                "action_type": 0
            },
            {
                "action_id": "Configuration update action id",
                "action_type": 6,
                "config": {
                    "interval": 10,
                    "servers": ["10.10.10.10", "1.2.3.4"]
                }
            }
        ]
    })
    resp.headers['Connection'] = 'close'
    return resp