from src.commands.get_all import GetAll
from src.commands.get import Get
from src.controllers.cli.base_cli import BaseCli
from argparse import ArgumentParser
from src.helpers.reports import to_csv, to_json
from src import app

@BaseCli.register
class Stocks():
  def __init__(self):
    pass
  
  def get_all(args):
    command = GetAll()
    try:
      df = command.execute()

      if args.export_csv:
        csv_file = to_csv(df, separator=";", export=True)
        print(f'Your csv file is available in {app.tmp_path}/{csv_file}')
      
      if args.export_json:
        json_file = to_json(df, export=True)
        print(f'Your json file is available in {app.tmp_path}/{json_file}')

      if not args.export_csv and not args.export_json:
        print(df)
    except Exception as e:
      # print(e)
      return None
  
  def get(args):
    command = Get(stock=args.stock)
    try:
      df = command.execute()
      if args.export_csv:
        csv_file = to_csv(df, separator=";", export=True)
        print(f'Your csv file is available in {app.tmp_path}/{csv_file}')

      
      if args.export_json:
        json_file = to_json(df, export=True)
        print(f'Your json file is available in {app.tmp_path}/{json_file}')

      if not args.export_csv and not args.export_json:
        print(df)
    except Exception as e:
      # print(e)
      return None
  

  def register_argument_parser(argparser: ArgumentParser):
    subparsers = argparser.add_subparsers(help='Functions')
    parser1 = subparsers.add_parser('get_all', help='Get all stocks available in fundamentus (result)')
    parser1.add_argument('--export-csv', help='Export data to csv', action='store_true')
    parser1.add_argument('--export-json', help='Export data to json', action='store_true')
    parser1.set_defaults(parser1=True, func=Stocks.get_all)
    
    parser2 = subparsers.add_parser('get', help='Get data from specific stock')
    parser2.add_argument('stock', type=str, help='Stock symbol (ex: TAEE11)')
    parser2.add_argument('--export-csv', help='Export data to csv', action='store_true')
    parser2.add_argument('--export-json', help='Export data to json', action='store_true')
    parser2.set_defaults(parser2=True, func=Stocks.get)
    
    args = argparser.parse_args()
    args.func(args)
