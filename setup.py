#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='0.2',
      packages=['dota2info'],
      package_data={"dota2info":["dota2info/templates/*",
                                 "dota2info/static/*"]},
      scripts=["scripts/dota2info_summary",
               "scripts/dota2info_combatlog",
               "scripts/dota2info_processDem",
               "scripts/dota2info_runTest",
               "scripts/dota2info_factionConflict"]
      )
