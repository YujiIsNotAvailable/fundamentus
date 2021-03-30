from flask import Flask
from pathlib import Path

def setup_tmp():
  basePath = Path(f'{app.root_path}').parent.absolute()
  tempPath = Path(
    f'{basePath}/tmp'
  )
  tempPath.mkdir(parents=True, exist_ok=True)
  app.tmp_path = str(tempPath)

app = Flask(__name__, template_folder='templates')
setup_tmp()