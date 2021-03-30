from abc import ABC, abstractmethod 
from argparse import ArgumentParser

class BaseCli(ABC):
  @staticmethod
  @abstractmethod 
  def register_argument_parser(arg: ArgumentParser):
    pass