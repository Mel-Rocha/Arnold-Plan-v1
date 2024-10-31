# Arnold Plan 💪 🔱

# Variáveis de Ambiente
## Postgres 🐘
- DB_ENGINE=postgresql
- DB_USERNAME=(nome do usuário do db)
- DB_PASS=(senha do usuário do db)
- DB_HOST=(seu ip)
- DB_PORT=5432
- DB_NAME=(nome do db)

caso as váriaveis de ambiente não sejam fornecidas, a aplicação
usará o mysql por padrão.

# Rodar Localmente 🏠

Passo 1 - Instale os módulos via VENV

```python
# Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Passo 2 - Configure o database

```python
python manage.py makemigrations
python manage.py migrate
```

* Passo 3 - De os comandos personalizados para criar e carregar o banco de informações nutricionais

```bash 
# Criar a tabela
python manage.py create_taco

# Carregar a tabela
python manage.py insert_taco
```


Passo 4 - Rode a aplicação

```python
python manage.py runserver
```

# Rodar com Docker 🐋
```python
docker compose build && docker compose up
```

---------

# Comandos Uteis Django 🚀
## Banco de Dados 🎲
 Permite execação de comandos SQL diretamente no banco de dados.

```bash
python manage.py dbshell
```

Visualizar todas as tabelas
```bash
\dt
``` 
Visualizar a estrutura de uma tabela
- Estrutura Básica
```bash
\d table_name  
```
- Estrutura Detalhada (incluindo informações adicionais como descrições de colunas, índices e tabelas associadas).
```bash 
\d+ table_name 
```

## Interagir com a API Django via shell 🖥️
```bash
python manage.py shell
```
Faça testes com suas models no shell
```bash
from django.contrib.auth.models import User

users = User.objects.all()
print(users)
```

Visualizar todas as urls do projeto
```bash
# Importar get_resolver
from django.urls import get_resolver

# Obter todas as URLs configuradas
urls = get_resolver().url_patterns

# Iterar sobre as URLs e imprimir cada uma
for url in urls:
    print(url)
```
----------------
# Template .env 📝
```bash
# GERAL
DEBUG="True"
SECRET_KEY="django-insecure-%%!5v*7a-v4cjkq%f85c3p7&=5u0wo06!nk5d9&@4b!k5tr"
ALLOWED_HOSTS="*"
CORS_ALLOWED_ORIGINS=http://localhost,http://127.0.0.1,https://example.com
CSRF_TRUSTED_ORIGINS=http://example.com,https://example.com

# DATABASE (DEFAULT SQLITE3)
DATABASE_URL="postgresql://user:password@localhost:5432/database_name"

# RETENTION
PG_HOST_RETENTION="localhost"
PG_PORT_RETENTION="5432"
PG_USER_RETENTION="user"
PG_PASSWORD_RETENTION="password"
DATABASE_RETENTION="database_name"

```