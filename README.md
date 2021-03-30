# Fundamentus python library #

## Requirements ##
Install dependences
```sh
cd fundamentus
pip install -r ./requirements.txt
```

## Run tests ##
```sh
python -m pytest
```

# CLI #
## Usage ##
```sh
  # Returns a dataframe like that:
  '''
    cotacao     p_l  p_vp    psr divyield  p_ativo  p_capgiro  p_ebit  ...  mrg_liq  liq_corr    roic      roe     liq2meses    patrim_liq divbrut_patrim cresc_rec5a
    papel                                                                      ...
    AALR3      8.82  -10.71  0.88  1.123    0,99%    0.411      11.29 -152.67  ...   -9,95%      1.19  -0,31%   -8,18%  6.754580e+06  1.190540e+09           0.67      -0,53%
    ABCB3      0.00    0.00  0.00  0.000    0,00%    0.000       0.00    0.00  ...    0,00%      0.00   0,00%    7,51%  0.000000e+00  4.288260e+09           0.00     -34,30%
    ABCB4     14.59   10.01  0.75  0.000    3,39%    0.000       0.00    0.00  ...    0,00%      0.00   0,00%    7,51%  1.283560e+07  4.288260e+09           0.00     -34,30%
    ABEV3     15.30   21.16  3.26  4.124    3,21%    1.923     129.11   17.52  ...   20,10%      1.06  15,58%   15,42%  3.819730e+08  7.381560e+10           0.06       6,05%
  ''' 
  python ./run.py get_all
  
  # Returns a dataframe like that:
  '''
         tipo    empresa             setor          subsetor cotacao data_ult_cot min_52_sem  ... p_ativos p_cap_giro  p_ativ_circ_liq  div_yield ev_ebitda ev_ebit cres_rec_5a
  papel                                                                                       ...
  TAEE11  UNT  TAESA UNT  Energia Elétrica  Energia Elétrica   38.40   29/03/2021      22.79  ...     0.94       8.71            -2.31       8,4%      7.76    7.81       27,0%
  '''
  python ./run.py get TAEE11

  # Optional arguments to export content to file 
  [--export-csv]
  [--export-json]
  #example
  python ./run.py get TAEE11 --export-json --export-csv
```

___
##~~WEB~~
under development..:grinning::grinning::grinning:
