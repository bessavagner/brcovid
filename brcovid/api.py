"""Esta API implementa ouso das funções em get_info.py
de forma indiscriminada ao local: se é estado ou cidade
"""

import json
import brcovid.get_info as get

def obter_dados(local):
    """

    Args:
        local (str): Sigla de estado ou nome de cidade.

    Returns:
        str: informações  dos casos de civd-19 do local.
    """
    if local in get.siglas_stados:
        return get.state_cases(local)
    else:
        return get.city_cases(local)
