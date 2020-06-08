"""Biblioteca que ler os dados convertidos do repositório:
https://github.com/turicas/covid19-br

Licenciado sobre LGPL-3.0

A licensa dos dados é Creative Commons Attribution ShareAlike.
"""
import requests
import json
import brcovid.brstates as states
from datetime import date, datetime, timedelta

API_BRASIL_IO = "https://brasil.io/api/dataset/covid19/caso_full/data"

states = states.initials

# sigla dos estados em letras maiúsculas:
siglas_stados = [key for key in states.keys()]

def date_format(data):
    """Formata a data em dia/mes/ano

    Args:
        data (str): data no formato ano-mes-dia

    Returns:
        str: data no formato dia/mes/ano
    """
    data = data.split('-')
    return f"{data[2]}/{data[1]}/{data[0]}"

def state_cases(state):
    """Retorna texto com os casos de covid-19 em um estado brasileiro

    Args:
        state (str): sigla de um estado (maiúscula)

    Returns:
        str: texto com os casos de covid-19 no estado
    """
    params = {'_is_last':True, 'place_type':'state'}
    data = requests.get(API_BRASIL_IO, params=params)
    message = "Não há registros"
    if data.ok:
        results = data.json()['results']
        cases = 0
        death = 0
        for result in results:
            if result['state'] == state:
                if result['is_last']:
                    message = f"Casos de covid-19 em {states[state]} - {date_format(result['date'])}\n"
                    message += f"Total de casos: {result['last_available_confirmed']}\n"+\
                                f"Total de mortos: {result['last_available_deaths']}\n"
                    message += f"Casos em 24h = {result['new_confirmed']}\n"
                    message += f"Morte em 24h = {result['new_deaths']}"
    return message


def city_cases(city):
    """Retorna texto com os casos de covid-19 uma cidade brasileira

    Args:
        state (str): uma cidade brasileira (primeira letra maiúscula)

    Returns:
        str: texto com os casos de covid-19 na cidade
    """
    data = requests.get(API_BRASIL_IO)
    if data.ok:
        page = data.json()
        cases = 0
        death = 0
        while True:
            results = page['results']
            for result in results:
                if result['city'] == city: 
                    if result['is_last']:
                        message = f"Casos de covid-19 em {result['city']}/{result['state']}"
                        message +=f" - {date_format(result['date'])}\n"
                        message += f"Total de casos: {result['last_available_confirmed']}\n"+\
                                   f"Total de mortos: {result['last_available_deaths']}\n"
                        message += f"Casos em 24h = {result['new_confirmed']}\n"
                        message += f"Morte em 24h = {result['new_deaths']}"
                        return message
            if page['next'] is None:
                return "Não há registros."
            else:
                data = requests.get(page['next'])
                if data.ok:
                    page = data.json()
                else:
                    return "Desculpe, não consegui ler os registros."

def list_cities():
    """
    Returns:
        str: Retorna lista de cidades brasileiras
        contidas no dataset do Brasil.IO
    """
    data = requests.get(API_BRASIL_IO)
    cities = []
    if data.ok:
        page = data.json()     
        while True:
            print(page['next'])
            if page['next'] is None:
                break
            results = page['results']
            for result in results:
                if result['city'] not in cities:
                    cities.append(result['city'])
            data = requests.get(page['next'])
            if data.ok:
                page = data.json()
            else:
                print("Something went wrong")
                break
    return cities
          