#!/usr/bin/env python
"""replace ~/ with /Users/username/ in ~/Library/LaunchAgents/*.plist"""
import os
import sys
import launchagents

"""
replace ~/ with /Users/username/
"""

USAGE = 'python -m launchagents.expanduser'

LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library", "LaunchAgents")


def expand(path=None):
    if not path:
        path = LAUNCHAGENTS
    files = launchagents.files()
    for f in files:
        old = open(f).read()
        new = old.replace("~/", "%s/" % os.environ["HOME"])
        if old != new:
            open(f, "w").write(new)


def _cli():
    path = LAUNCHAGENTS
    if len(sys.argv) == 2:
        path = sys.argv[1]
    expand(path)


if __name__ == '__main__':
    _cli()
