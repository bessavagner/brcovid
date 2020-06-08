import brcovid.api as brc
from brcovid import get_info
import numpy as np

local = 'Lagoa do Ouro'
print(brc.obter_dados(local))

"""lista = np.array(get_info.list_cities())

np.save('lista_cidades', lista)"""


