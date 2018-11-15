#!/usr/bin/env python
"""set Finder tags. `red` - error, `orange` - stderr, `gray` - unloaded"""
import os
import launchctl
import launchagents
import mac_colors


LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library", "LaunchAgents")


JOBS = launchctl.jobs()


def _job(label):
    for job in JOBS:
        if job.label == label:
            return job


def _tree(path, top):
    while path != os.path.dirname(top):
        yield path
        path = os.path.dirname(path)


def tag():
    """set Finder tags. `red` - error, `orange` - stderr, `gray` - unloaded"""
    path = LAUNCHAGENTS
    gray = []
    orange = []
    red = []
    files = launchagents.files()
    tree = []
    for f in files:
        paths = list(_tree(f, path))
        data = launchagents.read(f)
        job = _job(data.get("Label", None))
        if not job:
            gray += [f]
        if job and job.status != 0:  # error
            red += paths
        stderr = data.get("StandardErrorPath", "")
        if stderr and os.path.exists(stderr) and os.path.getsize(stderr) > 0:
            orange.append(f)
    none = list(filter(lambda p: p not in gray + orange + red, tree))
    mac_colors.none(none)
    mac_colors.gray(gray)
    mac_colors.orange(orange)
    mac_colors.red(red)


def _cli():
    tag()


if __name__ == '__main__':
    _cli()
