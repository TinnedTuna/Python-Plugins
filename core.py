from straight.plugin import load
from pack.worker import Worker
from pack.plugin import Plugin

plugins = load('pack.plugins', subclasses=Plugin)
#plugins = load('pack.plugins' )
for p in plugins:
  print("plugin name: " + p.plugin_name())
worker = Worker(plugins)
