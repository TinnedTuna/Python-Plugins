
class Plugin():
  def __init__(self):
    print ("loaded!")

  @classmethod
  def plugin_name(cls):
    return cls.__name__;
