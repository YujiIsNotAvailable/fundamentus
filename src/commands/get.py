from src.commands.abc_command import AbcCommand
from src.helpers.utils import normalize_str
from datetime import datetime
import pandas as pd

class Get(AbcCommand):
  def __init__(self, stock: str):
    super().__init__()
    self.stock = stock.upper()
  
  def _extract_tables_columns_and_values(self, tables):
    columns = []
    values = []

    df_sumary = tables[0]
    columns = list(df_sumary[0])
    values = list(df_sumary[1])
    
    columns = columns + list(df_sumary[2])
    values = values + list(df_sumary[3])

    df_market_value = tables[1]
    columns = columns + list(df_market_value[0])
    values = values + list(df_market_value[1])
    
    columns = columns + list(df_market_value[2])
    values = values + list(df_market_value[3])
    
    df_fundamentalist = tables[2].drop(0)
    columns = columns + list(df_fundamentalist[2])
    values = values + list(df_fundamentalist[3])
    return [columns, values]

  def _normalize_stock_raw(self, columns: list, values: list):
    stock_raw = {}
    for column in columns:
      value = columns.index(column)
      column = normalize_str(column)
      stock_raw[column] = values[value]
    return stock_raw
  
  def execute(self) -> pd.core.frame.DataFrame:
    content = self._do_request()    
    tables = pd.read_html(content.text, decimal=",", thousands='.')

    columns, values = self._extract_tables_columns_and_values(tables)
    stock_raw = self._normalize_stock_raw(columns, values)

    df = pd.DataFrame([stock_raw])
    df.index = df['papel']
    df.drop('papel', axis='columns', inplace=True)
    df.name=f'{self.stock}_details_{datetime.today().strftime("%d_%m_%Y_%H_%M_%S")}'
    return df
  
  def _do_request(self):
    return self.requests.get(f'{self.base_url}/detalhes.php?papel={self.stock}', 
      headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
      }
    )
  