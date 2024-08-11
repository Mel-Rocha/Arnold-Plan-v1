# Arnold Plan

# Variáveis de Ambiente
## Postgres
- DB_ENGINE=postgresql
- DB_USERNAME=(nome do usuário do db)
- DB_PASS=(senha do usuário do db)
- DB_HOST=(seu ip)
- DB_PORT=5432
- DB_NAME=(nome do db)

caso as váriaveis de ambiente não sejam fornecidas, a aplicação
usará o mysql.

# Rodar Localmente

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

Passo 3 - Rode a aplicação

```python
python manage.py runserver
```

# Rodar com Docker
```python
docker compose build && docker compose up
```

# Útil
## Como saber o ip (linux)

O host deve ser obtido por meio do seguinte comando que descobrirá o ip real
do servidor postgres (permitindo que o docker o localize).
```bash
ip a 
```