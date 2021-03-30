import pytest
import datatest as dt
import json
from src.commands.get_all import GetAll
from src.helpers.reports import to_csv, to_json
from src import app
from pathlib import Path


@pytest.fixture(scope='session')
def all_stocks_df():
  command = GetAll()
  return command.execute()

@pytest.fixture()
def export_to_json_file(all_stocks_df):
  filename = to_json(all_stocks_df, export=True)
  yield filename
  Path(f'{app.tmp_path}/{filename}').unlink()

@pytest.fixture()
def export_to_csv_file(all_stocks_df):
  filename = to_csv(all_stocks_df, export=True)
  yield filename
  Path(f'{app.tmp_path}/{filename}').unlink()

def test_get_all_stocks_columns(all_stocks_df):
   dt.validate(
    all_stocks_df.columns,
      {
        'cotacao', 'p_l', 'p_vp', 'psr', 'divyield', 'p_ativo', 'p_capgiro',
        'p_ebit', 'p_ativ_circliq', 'ev_ebit', 'ev_ebitda', 'mrg_ebit',
        'mrg_liq', 'liq_corr', 'roic', 'roe', 'liq2meses', 'patrim_liq',
        'divbrut_patrim', 'cresc_rec5a'
      }
    )

def test_get_all_count_register(all_stocks_df):
   assert len(all_stocks_df) > 1

'''
Should return something like that:
  {
    'AALR3': 
      {
        'cotacao': 8.84, 
        'p_l': -10.73,
        'p_vp': 0.88,
        'psr': 1.126,
        'divyield': '0,99%',
        'p_ativo': 0.412,
        'p_capgiro': 11.31,
        'p_ebit': -153.02,
        'p_ativ_circliq': -1.4,
        'ev_ebit': -235.65,
        'ev_ebitda': 14.34,
        'mrg_ebit': '-0,74%',
        'mrg_liq': '-9,95%',
        'liq_corr': 1.19,
        'roic': '-0,31%',
        'roe': '-8,18%',
        'liq2meses': 6475140.0,
        'patrim_liq': 1190540000.0,
        'divbrut_patrim': 0.67,
        'cresc_rec5a': '-0,53%'
      },
    'ABCB3': 
      {
        'cotacao': 0.0,
        'p_l': 0.0,
        'p_vp': 0.0,
        'psr': 0.0,
        'divyield': '0,00%',
        'p_ativo': 0.0,
        'p_capgiro': 0.0,
        'p_ebit': 0.0,
        'p_ativ_circliq': 0.0,
        'ev_ebit': 0.0,
        'ev_ebitda': 0.0,
        'mrg_ebit': '0,00%',
        'mrg_liq': '0,00%',
        'liq_corr': 0.0,
        'roic': '0,00%',
        'roe': '7,51%',
        'liq2meses': 0.0,
        'patrim_liq': 4288260000.0,
        'divbrut_patrim': 0.0,
        'cresc_rec5a': '-34,30%'
      }#continues..
'''
def test_to_json(all_stocks_df):
  json_loaded = json.loads(to_json(all_stocks_df))
  assert json_loaded

''' Export all stocks to json file located in /tmp/{filename} '''
def test_export_to_json(export_to_json_file):
  with open(f'{app.tmp_path}/{export_to_json_file}') as f:
    json_loaded = json.loads(f.read())
    assert json_loaded

''' Should return something like that:
  index;papel;cotacao;p_l;p_vp;psr;divyield;p_ativo;p_capgiro;p_ebit;p_ativ_circliq;ev_ebit;ev_ebitda;mrg_ebit;mrg_liq;liq_corr;roic;roe;liq2meses;patrim_liq;divbrut_patrim;cresc_rec5a
  0;AALR3;8.82;-10.71;0.88;1.123;0,99%;0.411;11.29;-152.67;-1.39;-235.31;14.31;-0,74%;-9,95%;1.19;-0,31%;-8,18%;6754580.0;1190540000.0;0.67;-0,53%
  1;ABCB3;0.0;0.0;0.0;0.0;0,00%;0.0;0.0;0.0;0.0;0.0;0.0;0,00%;0,00%;0.0;0,00%;7,51%;0.0;4288260000.0;0.0;-34,30%
'''
def test_to_csv(all_stocks_df):
  csv_loaded = to_csv(all_stocks_df)
  assert csv_loaded

''' Export all stocks to csv file located in /tmp/{filename} '''
def test_export_to_csv(export_to_csv_file):
  with open(f'{app.tmp_path}/{export_to_csv_file}') as f:
    assert f.read()