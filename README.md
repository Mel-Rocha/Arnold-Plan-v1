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
```bash
# Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

Passo 2 - Instale as dependências
```bash
pip install -r requirements.txt
```

Passo 3 - Execute o servidor
```bash
python manage.py runserver
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
