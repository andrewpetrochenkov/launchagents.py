#!/usr/bin/env python
import launchagents

path = "/tmp/update.plist"
data = {"Label": "Example"}
launchagents.update(path, **data)
assert data == launchagents.read(path)
