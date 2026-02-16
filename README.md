# Como usar o flask-boilerpate

## Clonar repositório

```
git clone git@github.com:jrdiniz/flask-boilerplate.git . 
```

## Criar ambiente virtual

Eu testei este projeto com a versão 3.12. Se você testar com outra versão, por favor, abra um pull request para atualizar a documentação.

```
python3.12 -m venv env
```

## Instalar dependências 

```
source env/bin/activate
pip install -r requirements.txt
```

## Configuração do ambiente

O projeto usa a biblioteca python-dotenv, então você precisa criar um arquivo .env no diretório raiz:

 - Ambiente de Desenvolvimento 

```
FLASK_APP=app
FLASK_DEBUG=True
FLASK_CONFIG_FILE=config.DevelopmentConfig
SECRET_KEY=<sua-chave-secreta>

```

 - Ambiente de Produção

```
FLASK_APP=app
FLASK_DEBUG=False
FLASK_CONFIG_FILE=config.ProductionConfig
SECRET_KEY=<sua-chave-secreta>

```

# Estrutura do projeto

```
.
├── app/                  # Código fonte do aplicativo
│   ├── __init__.py       # Inicialização do pacote
│   ├── config.py         # Configurações do aplicativo
│   └── blueprints        # Blueprint  
│       └── webui 
│           ├── __init_.py
│           ├── webui.py      
│   └── ...
├── env/                  # Ambiente virtual (não versionado)
├── requirements.txt      # Dependências do Python
├── Dockerfile            # Imagem do Docker
└── README.md             # Este arquivo
```

# Bibliotecas

 - Bootstrap5
 - Bootstrap Icons
 - HTMX

### Atualizar pacote NPM

```npx npm-check-updates -u```

```npm install```

## Implantar com Docker

Criar imagem da aplicação

```
docker build -t flask-boilerplate .
```

Para executar o contêiner

```
docker run -p <host-port>:5000 -d --name <project-name> flask-boilerplate
```

Para implantar o contêiner

```
docker exec -it <container-id> bash
```

## Implantar usando Ansible

Para implantar usando Ansible, certifique-se de que o Ansible esteja instalado e execute o seguinte comando:

```
ansible-playbook -i hosts deploy.yml
```

## Notas Finais

- Certifique-se de que as portas necessárias estejam abertas em seu firewall.
- Verifique os logs da aplicação para solucionar problemas: `docker logs <container-id>`.
- Para acessar o shell do contêiner em execução: `docker exec -it <container-id> /bin/bash`.

