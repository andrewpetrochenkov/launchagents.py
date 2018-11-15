[![](https://img.shields.io/pypi/pyversions/launchagents.svg?longCache=True)](https://pypi.org/pypi/launchagents/)
[![](https://img.shields.io/pypi/v/launchagents.svg?maxAge=3600)](https://pypi.org/pypi/launchagents/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchagents.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchagents.py/)

#### Install
```bash
$ [sudo] pip install launchagents
```

#### Classes

###### `launchagents.Agent`

launchd.plist LaunchAgent class

method|description
-|-
`create()`|create .plist file and stderr, stdout logs

#### Functions
function|description
-|-
`launchagents.files()`|return list of ~/Library/LaunchAgents .plist files
`launchagents.load()`|load ~/Library/LaunchAgents/*.plist
`launchagents.read(path)`|return dict with .plist data
`launchagents.tag()`|set Finder tags. `red` - error, `orange` - stderr, `gray` - unloaded
`launchagents.unload()`|unload ~/Library/LaunchAgents/*.plist

#### CLI
usage|description
-|-
`python -m launchagents.expanduser`|replace ~/ with /Users/username/ in ~/Library/LaunchAgents/*.plist
`python -m launchagents.list`|`launchctl list` for ~/Library/LaunchAgents/*.plist
`python -m launchagents.load`|load ~/Library/LaunchAgents/*.plist
`python -m launchagents.tag`|set Finder tags. `red` - error, `orange` - stderr, `gray` - unloaded
`python -m launchagents.unload`|unload ~/Library/LaunchAgents/*.plist

#### Examples
`path/to/agent.py`
```python
class MyAgent(launchagents.Agent):
    interval = 5  # StartInterval
    # watch     (WatchPaths)

    def run(self):
        pass

if __name__ == "__main__":
    MyAgent().run()
```

```python
>>> MyAgent().create().path
'path/to/agent.plist'
```

```bash
$ find ~/Library/LaunchAgents -name "*.plist" | xargs launchctl load
$ find ~/Library/LaunchAgents -name "*.plist" | xargs launchctl unload
$ launchctl list | grep -v "com."    # `launchctl` list without com.apple agents
```

#### Links
+   [launchd.plist(5) Mac OS](https://www.real-world-systems.com/docs/launchd.plist.5.html)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>