import os
import sys

sys.path.append(
  os.path.expanduser('~/.inv/')
)

class Spec:

  def use(self) -> None:
    print("You try it, but it doesn't do anything.")
    return None

class items:

  import types

  @staticmethod
  def use(item: str):
    import importlib
    object = importlib.import_module(f"{item}")
    instance = getattr(object, item)()
    return instance.use()
