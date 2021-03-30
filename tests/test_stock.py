import pytest
import datatest as dt
from src.commands.get import Get

@pytest.fixture(scope='session')
def stock_symbol():
  return 'TAEE11'

@pytest.fixture(scope='session')
def stock_df(stock_symbol):
  symbol = stock_symbol
  command = Get(symbol)
  return command.execute()

'''
Check if broughts all the columns correctly
'''
@pytest.mark.mandatory
def test_get_stock_columns(stock_df, stock_symbol):
  dt.validate(
    stock_df.columns,
    {
      'tipo', 'empresa', 'setor', 'subsetor', 'cotacao', 'data_ult_cot',
      'min_52_sem', 'max_52_sem', 'vol_med_2m', 'valor_de_mercado',
      'valor_da_firma', 'ult_balanco_processado', 'nro_acoes', 'p_l', 'p_vp',
      'p_ebit', 'psr', 'p_ativos', 'p_cap_giro', 'p_ativ_circ_liq',
      'div_yield', 'ev_ebitda', 'ev_ebit', 'cres_rec_5a'
    }
  )

'''
Check if broughts all the values correctly
'''
@pytest.mark.mandatory
def test_get_stock_values(stock_df, stock_symbol):
  df = stock_df
  dt.validate(df['tipo'], str)
  dt.validate(df['empresa'], str)
  dt.validate(df['setor'], str)
  dt.validate(df['subsetor'], str)
  dt.validate(df['cotacao'], str)
  dt.validate(df['data_ult_cot'], str)
  dt.validate(df['min_52_sem'], str)
  dt.validate(df['max_52_sem'], str)
  dt.validate(df['vol_med_2m'], str)
  dt.validate(df['valor_de_mercado'], int)
  dt.validate(df['valor_da_firma'], int)
  dt.validate(df['ult_balanco_processado'], str)
  dt.validate(df['nro_acoes'], str)
  dt.validate(df['p_l'], str)
  dt.validate(df['p_vp'], str)
  dt.validate(df['p_ebit'], str)
  dt.validate(df['psr'], str)
  dt.validate(df['p_ativos'], str)
  dt.validate(df['p_cap_giro'], str)
  dt.validate(df['p_ativ_circ_liq'], str)
  dt.validate(df['div_yield'], str)
  dt.validate(df['ev_ebitda'], str)
  dt.validate(df['ev_ebit'], str)
  dt.validate(df['cres_rec_5a'], str)

'''
Check if broughts the correct stock
'''
@pytest.mark.mandatory
def test_get_stock(stock_df, stock_symbol):
  df = stock_df
  assert df.index[0] == stock_symbol