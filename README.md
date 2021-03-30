# Footprinting WordPress
## Saída do WpScan tratada

Footprinting WordPress é um script escrito em python no formato de RestFull API, que faz a leitura da saída do wpscan e devolve um json com as informações tratadas, tudo através de uma requisição POST no servidor web local criado.

## Features

- Criação de API em Python com poucas linhas de código
- Leitura, escrita e saída em JSON
- Leitura da saída do WpScan
- Tratamento das informações coletadas pelo WpScan
- Fácil de rodar e pode ser reutilizado para outras ferramentas

## Tech

Foi utilizado alguns projetos de código aberto:

- [Python] - Linguagem utilizada para desenvolver o script.
- [Flask] - Framework web para criação da API.
- [WpScan] - Ferramenta que busca informações em apps WordPress.

## Installation

Para conseguir usar a ferramenta, você vai precisar de um arquivo JSON com a saída do WpScan que você tenha executado em algum site WordPress.

```sh
wpscan --url http://sitewordpress.com/ -f json -o wpscan
```
Foi utilizado o python 3.9.2 na PoC.

Baixe o projeto, acesse a pasta footprinting e com um python3 instale o flask através do pip.

```sh
git clone https://github.com/jmessiass/footprinting.git
cd footprinting
pip install flask
```

## How to Use

Após ter feito os passos acima basta rodar o script api.py.

```sh
python api.py
```

Será criado uma API na porta 5000, basta realizar o curl abaixo na sua API criada, passando o arquivo JSON do WpScan, aqui chamado de wpscan.

```sh
curl -X POST -H "Content-Type: application/json" -d '{"url":"~/wpscan"}' http://localhost:5000/wordpress
```

Após realizar a requição POST, a ferramenta vai retornar um JSON com as informações tratadas, retornando apenas o que enxergo de importante para uma fase de information gathering, podendo o script ser customizado e adaptado para os cenários que quiserem.