import brcovid.api as brc
from brcovid import get_info
import numpy as np

local = 'São Luís'
print(brc.obter_dados(local))
# get_info.city_cases('São Luís')

"""lista = np.array(get_info.list_cities())

np.save('lista_cidades', lista)"""


