# brcovid

Pacote python para exibir os casos de covid-19 no Brasil em forma de texto simples:

 ~~~terminal
Casos de <local> - <data>
Total de casos: <número>
Total de mortos: <número>
Casos em 24h = <número>
Morte em 24h = <número>
~~~

## API

A integração com so dados utilizado é feita através do módulo ```brcovid.get_info```, que por sua vez lê a API de dados convertidos do [covid19-br](https://github.com/turicas/covid19-br).

O a API deste pacote é apenas o módulo ```brcovid.api``` de única função ```obter_dados```, cujo argumento deve ser uma sigla de estado ou cidade brasileira.

## Licença e citação

Como os dados utilizado estão sob licensa [Creative Commons Attribution ShareAlike](https://creativecommons.org/licenses/by-sa/4.0/), este pacote segue a mesma licensa.

## Fonte

- Brasil.IO: boletins epidemiológicos da COVID-19 por município por dia, disponível no [data set do covid18-br](https://brasil.io/dataset/covid19/)

Os dados utilizado por este pacote foram organizado por [40 voluntários](https://brasil.io/covid19/voluntarios/) no projeto [Brasil.IO](https://brasil.io/covid19/) que, diariamente, compilam boletins epidemiológicos das 27 Secretarias Estaduais de Saúde.

## Requisitos

Você precisará ter Python >= 3.6 instalado e pip >=19.2.3, assim como o módulo ```requests```, o qual é instalado com este pacote caso não possua.

Pode ser que funcione em outras versão. Se a sua é inferior, envie um *pull request* para atualizar este README.md.

## Instalação

Baixe ou clone o repositório numa pasta em seu computador, então, no terminal de comando aberto na pasta rode:

~~~temrinal
pip install .
~~~

## Uso

Segue o exemplo de uso contido no arquivo [exemplo.py](https://github.com/bessavagner/brcovid/exemplo.py):

~~~python
import brcovid.api as brc

local = 'Crateús'

print(brc.obter_dados(local))
~~~

## Agradecimentos

- Insitutto Federal de Ciência e Tecnologia do Estado do Ceará.
- [Brasil.IO](https://brasil.io/)

## Sobre o autor

- [Vagner Bessa](https://github.com/bessavagner/) - Físico e professor.
