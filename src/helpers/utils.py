import re

def normalize_str(string: str):
  string = string.lower()
  string = re.sub('[?()$.,]', '', string)
  string = re.sub('[ç]'  , 'c' , string)
  string = re.sub('[âáãà]', 'a' , string)
  string = re.sub('[ôóõò]', 'o' , string)
  string = re.sub('[êé]' , 'e' , string)
  string = re.sub('[îí]' , 'i' , string)
  string = re.sub('[ûú]' , 'u' , string)
  string = re.sub('[ÛÚ]' , 'U' , string)
  string = re.sub(' \\/ ', '_', string)
  string = re.sub('[ /]'  , '_' , string)
  string = re.sub('__'   , '_' , string)
  return string
