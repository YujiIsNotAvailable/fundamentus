from abc import ABC, abstractmethod
import requests

class AbcCommand(ABC):
  def __init__(self):
    self.requests = requests
  
  @abstractmethod
  def execute():
    pass

  @property
  def base_url(self) -> str:
    return 'http://www.fundamentus.com.br'