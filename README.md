<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/launchagents.svg?longCache=True)](https://pypi.org/project/launchagents/)
[![](https://img.shields.io/pypi/v/launchagents.svg?maxAge=3600)](https://pypi.org/project/launchagents/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchagents.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchagents.py/)

#### Installation
```bash
$ [sudo] pip install launchagents
```

#### Features
+   works with `~/Library/LaunchAgents/` only

#### Functions
function|`__doc__`
-|-
`launchagents.files()` |return a list of `~/Library/LaunchAgents/*.plist` files
`launchagents.jobs()` |return a list of launchctl jobs for `~/Library/LaunchAgents/*.plist` only
`launchagents.load()` |load `~/Library/LaunchAgents/*.plist`
`launchagents.read(path)` |return a dictionary with a plist file data
`launchagents.unload()` |unload `~/Library/LaunchAgents/*.plist`
`launchagents.update(path, **kwargs)` |update a plist file
`launchagents.write(path, data)` |write a dictionary to a plist file

#### Links
+   [launchd.plist(5) Mac OS](https://www.real-world-systems.com/docs/launchd.plist.5.html)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>