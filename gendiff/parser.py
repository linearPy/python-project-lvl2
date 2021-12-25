import json
import yaml


def deserialize(path):
    file = open(path)

    if path.endswith('.json'):
        return json.load(file)
    if path.endswith('.yml') or path.endswith('.yaml'):
        return yaml.safe_load(file)
