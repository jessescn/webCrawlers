# Turmas Ofertadas

Crawler para baixar as turmas ofertadas no controle acadêmico

## Configuração

### Credenciais

A matricula e senha do controle academico são configurados localmente no arquivo .env. Para isso é necessário criar um arquivo .env, copiar e colar os campos do arquivo .env.example e preencher com credenciais válidas.

```bash
# arquivo .env

MATRICULA=
SENHA=

```

### Instalação

Pode ser executado de dentro de um ambiente de desenvolvimento, utilizando o pipenv ou instalando as dependências na máquina.

```bash
# Instalação do pipenv

$ pip3 install pipenv
$ cd turmasOfertadas && pipenv install

# Instalação das dependências na máquina
$ pip3 install --user scrapy python-dotenv
```

### Execução

O arquivo principal é o **run.py**, podendo ser executado tanto pelo script dentro do pipenv (caso tenha escolhido a opção de _local environment_) ou executando a partir do python3 mesmo (caso tenha instalado as dependências na sua máquina)

```bash
$ pipenv run crawler

ou

$ python3 run.py
```