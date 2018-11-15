#!/usr/bin/env python
import os
import sys
import public
import launchd_plist

LAUNCHAGENTS = os.path.join(os.environ["HOME"], "Library/LaunchAgents")
LOGS = os.path.join(os.environ["HOME"], "Library/Logs/LaunchAgents")

# `launchagents.Agent` - generate `.plist` agent from class. `launchd.plist` keys as class attributes


class Agent(launchd_plist.Plist):
    """launchd.plist LaunchAgent class"""
    __readme__ = ["create"]
    interval = None
    watch = []
    _label = None
    _script = None
    _args = None
    _stdout = None
    _stderr = None

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if v:
                setattr(self, k, v)

    @property
    def Label(self):
        return getattr(self, "label", None)

    @Label.setter
    def Label(self, label):
        self.label = label

    @property
    def StartInterval(self):
        return getattr(self, "interval", None)

    @StartInterval.setter
    def StartInterval(self, interval):
        self.interval = interval

    @property
    def StartCalendarInterval(self):
        return getattr(self, "calendar", None)

    @StartCalendarInterval.setter
    def StartCalendarInterval(self, data):
        self.calendar = dict(data)

    @property
    def WatchPaths(self):
        return getattr(self, "watch", None)

    @WatchPaths.setter
    def WatchPaths(self, paths):
        self.watch = list(paths)

    @property
    def ProgramArguments(self):
        return getattr(self, "args", None)

    @ProgramArguments.setter
    def ProgramArguments(self, args):
        self.watch = list(args)

    @property
    def StandardOutPath(self):
        return getattr(self, "stdout", None)

    @StandardOutPath.setter
    def StandardOutPath(self, path):
        self.stdout = str(path)

    @property
    def StandardErrorPath(self):
        return getattr(self, "stderr", None)

    @StandardErrorPath.setter
    def StandardErrorPath(self, path):
        self.stderr = str(path)

    """
predefined keys:
label (Label)
args (ProgramArguments)
stdout (StandardOutPath)
stderr (StandardErrorPath)
    """

    @property
    def label(self):
        if self._label:
            return self._label
        if not os.path.exists(self.script):
            raise ValueError("'%s' NOT EXISTS" % self.script)
        path = self.script[:-3]
        for r in [LAUNCHAGENTS, os.environ["HOME"]]:
            path = path.replace("%s/" % r, "")
        label = ".".join(path.replace(" ", "-").split("/"))
        if label.find("py.") != 0:
            label = "py.%s" % label
        return label

    @label.setter
    def label(self, label):
        self._label = label

    @property
    def path(self):
        if not self.label:
            raise ValueError("empty label")
        return os.path.join(LAUNCHAGENTS, "%s.plist" % self.label)

    @property
    def args(self):
        if self._args:
            return self._args
        """
`bash -l` load environment variables
        """
        return ["bash", "-l", "-c", "python %s %s" % (self.script, self.path)]

    @property
    def script(self):
        if self._script:
            return self._script
        return sys.modules[self.__class__.__module__].__file__

    @property
    def stdout(self):
        return os.path.join(LOGS, self.label, "out.log")

    @property
    def stderr(self):
        return os.path.join(LOGS, self.label, "err.log")

    def create(self):
        """create .plist file and stderr, stdout logs"""
        launchd_plist.Plist.create(self, self.path)
        return self

    def __str__(self):
        return "<Agent %s>" % str(self.data)

    def __repr__(self):
        return "<Agent %s>" % str(self.Label)
