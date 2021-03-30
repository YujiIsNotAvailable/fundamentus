from src.commands.abc_command import AbcCommand
from src.helpers.utils import normalize_str
from datetime import datetime
import pandas as pd

class GetAll(AbcCommand):
  def __init__(self):
    super().__init__()

  def execute(self) -> pd.core.frame.DataFrame:
    content = self._do_request()    
    df = pd.read_html(content.text, decimal=",", thousands='.')[0]
    df.index = df['Papel']
    df.drop('Papel', axis='columns', inplace=True)
    df.index.name = normalize_str('Papel')
    df.sort_index(inplace=True)
    df.name=f'all_stocks_{datetime.today().strftime("%d_%m_%Y_%H_%M_%S")}'

    df.columns = [normalize_str(i) for i in list(df.columns)]

    return df
  
  def _do_request(self):
    return self.requests.get(f'{self.base_url}/resultado.php', 
      headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
      }
    )