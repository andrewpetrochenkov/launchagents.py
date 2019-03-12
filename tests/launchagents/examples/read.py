#!/usr/bin/env python
import launchagents

path = "/System/Library/LaunchAgents/com.apple.Finder.plist"
if launchagents.MAC:
    data = launchagents.read(path)
    print(data)
