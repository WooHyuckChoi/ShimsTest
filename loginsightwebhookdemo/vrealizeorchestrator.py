#!/usr/bin/env python

from loginsightwebhookdemo import app, parse, sendevent
from flask import request, json
import base64
import re

__author__ = "John Dias"
__license__ = "Apache v2"
__version__ = "1.1"


# vRealize Orchestrator server workflow hostname (or hostname:port)
VROHOSTNAME = ''



@app.route("/endpoint/vro/<WORKFLOWID>", methods=['POST'])
@app.route("/endpoint/vro/<WORKFLOWID>/<ALERTID>", methods=['PUT'])
def vro(WORKFLOWID=None, ALERTID=None):
    """
    Start a vRealize Orchestrator workflow, passing the entire JSON alert as a base64-encoded string.
    The `WORKFLOWID` is passed in the webhook URL.
    The workflow is responsible for parsing base64 -> json -> messages
    """
    if not WORKFLOWID:
        return ("WORKFLOWID must be set in the URL (e.g. /endpoint/vro/<WORKFLOWID>", 500, None)
    if not re.match('[a-z0-9-]+', WORKFLOWID, flags=re.IGNORECASE):
        return ("WORKFLOWID must consist of alphanumeric and dash characters only", 500, None)
    if not VROHOSTNAME:
        return ("VROHOSTNAME parameter must be set, please edit the shim!", 500, None)

    a = parse(request)

    payload = {
        "parameters": [
            {
                "value": {
                    "string": {
                        "value": base64.b64encode(request.get_data())
                    }
                },
                "type": "string",
                "name": "messages",
                "scope": "local"
            },
            {
                "value": {
                    "string": {
                        "value": a['AlertName']
                    }
                },
                "type": "string",
                "name": "alertName",
                "scope": "local"
            },
            {
                "value": {
                    "number": {
                        "value": a['NumHits']
                    }
                },
                "type": "number",
                "name": "hitCount",
                "scope": "local"
            }
        ]
    }
    return sendevent("https://" + VROHOSTNAME + "/vco/api/workflows/" + WORKFLOWID + "/executions", json.dumps(payload))
