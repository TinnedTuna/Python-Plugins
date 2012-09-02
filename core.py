from straight.plugin import load
from pack import Worker
from pack.plugins import Plugin

#plugins = load('pack.plugins', subclasses=Plugin)
plugins = load('pack.plugins')
worker = Worker.Worker(plugins)
