import json

class SummaryEncoder(json.JSONEncoder):
    """ This class is used to convert the Player object to a json dict """
    def default(self, obj):
       if isinstance(obj, Player):
          return obj.get_dict()
       return json.JSONEncoder.default(self, obj)

def getCombatlogsTranslated(replay):
    """ assumes the replay consists of linewise json.loads 
    products, from the raw .demson

    filters for gameevent combatlogs, 
    replaces all ids by strings from the stringtable 
    """
    #The last replay combatlog stringtable. (which is complete)
    tr = filter(lambda ge: ge['demsontype'] == 'stringtable' and \
        ge['tablename'] == "CombatLogNames", replay)[-1]['stringtable']
    # Note: tr stands for translate.
    to_tr = ('attackername', 'inflictorname', 'sourcename', 'targetname', 'targetsourcename')

    combatlogs = filter(lambda ge: ge['demsontype'] == 'gameevent' and ge['evname'] == 'dota_combatlog', replay)
    combatlogs_tr = map(lambda ge: {k: tr[v] if k in to_tr else v for k, v in ge.iteritems()}, combatlogs)

    return combatlogs_tr
