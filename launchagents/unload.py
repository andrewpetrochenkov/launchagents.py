#!/usr/bin/env python
"""unload ~/Library/LaunchAgents/*.plist"""
import os
import sys
import launchagents

LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library", "LaunchAgents")


def _unload(path):
    files = launchagents.files(path)
    launchagents.unload(files)


def _cli():
    path = LAUNCHAGENTS
    if len(sys.argv) == 2:
        path = sys.argv[1]
    _unload(path)


if __name__ == '__main__':
    _cli()
