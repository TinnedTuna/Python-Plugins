from pack.plugin import Plugin

class ExtendingPlugin(Plugin):
  pass

if __name__=="__main__":
  p = ExtendingPlugin()
  print(p.plugin_name())
