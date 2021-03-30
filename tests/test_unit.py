import pytest
import inspect
import argparse
import os
import importlib
from src.helpers.utils import normalize_str
from src import app
from src.controllers.cli.base_cli import BaseCli
from stringcase import pascalcase

@pytest.mark.parametrize('weird_str, normalized_str', [
  ('?Papel', 'papel'), 
  ('Mrg. Liquida', 'mrg_liquida'),
  ('P / L', 'p_l'),
  ('P/L', 'p_l'),
  ('m(a)', 'ma'),
  ('Elétrica', 'eletrica'),
  ('Ação Íí', 'acao_ii'),
  ('Lucro__Líquido', 'lucro_liquido'),
  ('Patrimonio / Líquido', 'patrimonio_liquido'),
  ('olá, jovem. ok? âáàóòôç', 'ola_jovem_ok_aaaoooc'),
])
def test_normalize_str(weird_str, normalized_str):
  assert normalize_str(weird_str) == normalized_str

@pytest.mark.skip(reason="no way for test this argparser")
def test_argparser():
  parser = argparse.ArgumentParser()
  try:
    for filename in os.listdir(f'{app.root_path}/controllers/cli'):
      module = f'src.controllers.cli.{filename[:-3]}'
      cliFile = importlib.import_module(module)
      cliController = getattr(cliFile, pascalcase(filename[:-3]))
      if inspect.isabstract(cliController) or not issubclass(cliController, BaseCli):
        continue
      cliController.register_argument_parser(parser) # Register all arguments 
  except Exception as e:
    pass