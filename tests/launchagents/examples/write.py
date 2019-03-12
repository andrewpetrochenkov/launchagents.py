#!/usr/bin/env python
import launchagents

path = "/tmp/write.plist"
data = {"Label": "Example"}
launchagents.write(path, data)
assert data == launchagents.read(path)
