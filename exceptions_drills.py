# Exercise: write a function that reads a JSON file and returns an empty dict if file missing or malformed.

import json


def read_json_file(path: str):
    try:
        with open(path, 'r') as json_file:
            json_dict_from_file = json.load(json_file)
    except FileNotFoundError as e:
        print(f'File: {path} not found')
        return {}
    except Exception as e:
        return {}
    else:
        return json_dict_from_file
    finally:
        print('read_json_file function ended')
4


