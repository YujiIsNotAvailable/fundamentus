from src.commands.abc_command import AbcCommand
from stringcase import pascalcase, snakecase
import importlib

def from_command_str(command: str) -> AbcCommand:
  try:
    commandClass = importlib.import_module('src.commands.'+command)
    return getattr(commandClass, pascalcase(command))
  except Exception as e:
    print(e)
    return None