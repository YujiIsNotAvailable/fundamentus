import pytest
import argparse
import pandas
from src import app
import json
from src.controllers.cli.stocks import Stocks

def test_stock():
  args = argparse.Namespace()
  args.export_csv = False
  args.export_json = False
  assert isinstance(Stocks.get_all(args), pandas.DataFrame)

def test_stock_export_csv():
  args = argparse.Namespace()
  args.export_csv = True
  args.export_json = False
  file = Stocks.get_all(args)
  with open(f'{app.tmp_path}/{file}') as f:
    assert f.read()

def test_stock_export_json():
  args = argparse.Namespace()
  args.export_csv = False
  args.export_json = True
  file = Stocks.get_all(args)
  with open(f'{app.tmp_path}/{file}') as f:
    json_loaded = json.loads(f.read())
    assert json_loaded

def test_stocks():
  args = argparse.Namespace()
  args.stock = 'WEGE3'
  args.export_csv = False
  args.export_json = False
  assert isinstance(Stocks.get(args), pandas.DataFrame)

def test_stocks_export_csv():
  args = argparse.Namespace()
  args.stock = 'WEGE3'
  args.export_csv = True
  args.export_json = False
  file = Stocks.get(args)
  with open(f'{app.tmp_path}/{file}') as f:
    assert f.read()

def test_stocks_export_json():
  args = argparse.Namespace()
  args.stock = 'WEGE3'
  args.export_csv = False
  args.export_json = True
  file = Stocks.get(args)
  with open(f'{app.tmp_path}/{file}') as f:
    json_loaded = json.loads(f.read())
    assert json_loaded