dota2info
=========

Ready for world domination

Python tools for Dota 2 .demson replays - linewise json formatted information extracted from .dem files. 
Based on dota2py.

Web API client
--------------

A thin wrapper around the Dota 2 web API described at:
[http://dev.dota2.com/showthread.php?t=47115](http://dev.dota2.com/showthread.php?t=47115)

This uses either the [requests](http://docs.python-requests.org/en/latest/index.html) library (dota2py/api.py), or [Twisted](http://www.twistedmatrix.com) (dota2py/twisted/api.py)

.demson Parser
--------------
To show a summary of useful information from a .demson, run summary.py or dota2info_summary (this functionality is a work in progress)
