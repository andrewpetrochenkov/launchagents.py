#!/usr/bin/env python
import launchagents

if launchagents.MAC:
    jobs = launchagents.jobs()
    for j in jobs:
        print(j)
