#!/usr/bin/env python
"""`launchctl list` for ~/Library/LaunchAgents/*.plist"""
import os
import sys
import columnate
import launchctl
import launchagents

LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library", "LaunchAgents")


JOBS = launchctl.jobs()


def _job(label):
    for job in JOBS:
        if job.label == label:
            return job


def _list(path):
    files = launchagents.files(path)
    matrix = []
    for f in files:
        data = launchagents.read(f)
        job = _job(data.get("Label", None))
        if job:
            r = [job.pid if job.pid else "-", job.status, job.label]
            matrix.append(r)
    if matrix:
        print(columnate.lists(matrix))


def _cli():
    path = LAUNCHAGENTS
    if len(sys.argv) == 2:
        path = sys.argv[1]
    _list(path)


if __name__ == '__main__':
    _cli()
