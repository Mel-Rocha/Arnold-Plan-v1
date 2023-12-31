# Arnold Plan

# Manual Build

Passo 1 - Clone o repositório para sua máquina local.

```python
git clone https://github.com/Mel-Rocha/Arnold-Plan/tree/documentation/baseline_3
cd source/source
```

Passo 2 - Instale os módulos via VENV

```python
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Passo 3 - Configure o database

```python
python manage.py makemigrations
python manage.py migrate
```

Passo 4 - Crie um superuser

```python
python manage.py createsuperuser
```

Passo 5 - Rode a aplicação

```python
python manage.py runserver
```