#!/usr/bin/env python
import os
import launchagents

path = os.path.join(os.path.dirname(__file__), "com.google.keystone.agent.plist")

data = launchagents.read(path)
print(data)
