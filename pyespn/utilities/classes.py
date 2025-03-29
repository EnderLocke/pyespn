import json
from pyespn.exceptions import JSONNotProvidedError


def check_json(json_obj):
    try:
        if isinstance(json_obj, dict):
            return
        parsed_json = json.loads(json_obj)
        if isinstance(parsed_json, dict):
            return
    except json.JSONDecodeError as e:
        raise JSONNotProvidedError(error_message=e.msg)
