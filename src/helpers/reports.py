from src import app
import json
import pandas as pd

def to_csv(df, filename: str = '', separator: str = ';', export: bool=False) -> str:
  if not filename:
    filename = f'{df.name}.csv'
  try :
    if export:
      df.to_csv(f'{app.tmp_path}/{filename}', sep=separator, index=False)
    else: 
      return df.to_csv(sep=separator, index=False)
    return filename
  except Exception as e:
    # print(e)
    return ''

def to_json(df, filename: str = '', export: bool=False) -> str:
  if not filename:
    filename = f'{df.name}.json'
  try :
    df.reset_index(inplace=True)
    obj = json.loads(df.to_json(orient="index"))
    data = {obj[key].pop('papel'): obj[key] for key in obj}

    if export:
      with open(f'{app.tmp_path}/{filename}', 'w') as jsonFile:
        json.dump(data, jsonFile)
    else:
      return json.dumps(data)
    return filename
  except Exception as e:
    # print(e)
    return ''