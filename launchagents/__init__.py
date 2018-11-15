#!/usr/bin/env python
import plistlib
import os
import public
import runcmd
import values
import listify
from launchagents.agent import Agent
from launchagents.tag import tag

LAUNCHAGENTS = "%s/Library/LaunchAgents" % os.environ["HOME"]


public.add(Agent, tag)


@listify.listify
@public.add
def files():
    """return list of ~/Library/LaunchAgents .plist files"""
    for root, dirs, files in os.walk(LAUNCHAGENTS):
        for f in files:
            if os.path.splitext(os.path.basename(f))[1] == ".plist":
                yield os.path.join(root, f)


@public.add
def read(path):
    """return dict with .plist data"""
    return plistlib.readPlist(path)


@public.add
def load():
    """load ~/Library/LaunchAgents/*.plist"""
    args = ["launchctl", "load"] + files()
    runcmd.run(args)._raise()


@public.add
def unload():
    """unload ~/Library/LaunchAgents/*.plist"""
    args = ["launchctl", "unload"] + files()
    runcmd.run(args)._raise()
