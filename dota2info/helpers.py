import json

class SummaryEncoder(json.JSONEncoder):
""" This class is used to convert the Player object to a json dict """
    def default(self, obj):
       if isinstance(obj, Player):
          return obj.get_dict()
       return json.JSONEncoder.default(self, obj)

