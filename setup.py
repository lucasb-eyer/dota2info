#!/usr/bin/env python

from distutils.core import setup

setup(name='Distutils',
      version='0.1',
      packages=['dota2info'],
      package_data={"dota2info":[]},
      scripts=["scripts/dota2info_summary",
               "scripts/dota2info_combatlog",
               "scripts/dota2info_factionConflict"]
      )
