import os
import json


_blacklist = []


def validate(username):
    """
    Used to check if username is in blacklist.
    """

    username = username.strip()
    username = username.lower()

    for word in _get_blacklist():
        if username == word:
            return False

    return True


def _get_blacklist():
    global _blacklist

    if not _blacklist:
        _blacklist = _load()

    return _blacklist


def _load():
    data_path = "%s/data/list.json" % os.path.dirname(
        os.path.abspath(__file__))

    with open(data_path, "r") as data_file:
        data_json = data_file.read()
    data_file.close()

    return json.loads(data_json)
