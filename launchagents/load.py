#!/usr/bin/env python
"""load ~/Library/LaunchAgents/*.plist"""
import os
import sys
import launchagents

LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library", "LaunchAgents")


def _load(path):
    files = launchagents.files(path)
    launchagents.load(files)


def _cli():
    path = LAUNCHAGENTS
    if len(sys.argv) == 2:
        path = sys.argv[1]
    _load(path)


if __name__ == '__main__':
    _cli()
