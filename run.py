from src.commands import factory
import argparse
import inspect
import os
import importlib
from stringcase import pascalcase
from src import app
from src.controllers.cli.base_cli import BaseCli

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  for filename in os.listdir(f'{app.root_path}/controllers/cli'):
    try:
      module = f'src.controllers.cli.{filename[:-3]}'
      cliFile = importlib.import_module(module)
      cliController = getattr(cliFile, pascalcase(filename[:-3]))
      if inspect.isabstract(cliController) or not issubclass(cliController, BaseCli): 
        continue
      cliController.register_argument_parser(parser) # Register all arguments 
    except Exception as e:
      # print(e)
      pass

  