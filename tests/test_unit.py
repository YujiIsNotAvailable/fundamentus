import pytest
from src.helpers.utils import normalize_str

@pytest.mark.parametrize('weird_str, normalized_str', [
  ('?Papel', 'papel'), 
  ('Mrg. Liquida', 'mrg_liquida'),
  ('P / L', 'p_l'),
  ('P/L', 'p_l'),
  ('m(a)', 'ma'),
  ('Elétrica', 'eletrica'),
  ('Ação Íí', 'acao_ii'),
  ('Lucro__Líquido', 'lucro_liquido'),
  ('Patrimonio / Líquido', 'patrimonio_liquido'),
  ('olá, jovem. ok? âáàóòôç', 'ola_jovem_ok_aaaoooc'),
])
def test_normalize_str(weird_str, normalized_str):
  assert normalize_str(weird_str) == normalized_str