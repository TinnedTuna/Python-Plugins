
class Worker(object):
  def __init__(self, plugins):
    self.plugins = set()
    for P in plugins:
      print(P.plugin_name())
      p = P()
      self.plugins.add(p)

