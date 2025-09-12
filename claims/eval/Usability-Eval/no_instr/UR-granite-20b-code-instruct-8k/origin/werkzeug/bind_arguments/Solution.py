from werkzeug.routing import BaseConverter

class Rule(BaseConverter):
    def __init__(self, url_map, rule):
        self.map = url_map
        self.rule = rule

class Dispatch(object):
    def __init__(self, app, map):
        self.map = map
        self.app = app
