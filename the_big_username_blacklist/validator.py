import os
import json


_blacklist = []


def validate(word):
    """
    Used to check if username is in blacklist.
    """

    word = word.strip()
    word = word.lower()

    return word not in get_blacklist()


def get_blacklist():
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
