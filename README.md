# README

<aside>
💪🏽 Construindo Atletas, trazendo novos talentos aos palcos.

</aside>

**************Índice**************

# O Projeto

O software é um projeto de estudos autoral desenvolvido para a faculdade, onde o aluno deve criar uma solução tecnológica inovadora e viável financeiramente. Leva em conta conceitos de engenharia de software como levantamento de requisitos, diagramação, modelagem e implementação até ter como produto final a aplicação web implementada.

# Tecnologias

- Python;
- Django;
- ChartJs.

# O Software

Aplicação web gratuita pensada para atletas iniciantes e entusiastas do fisiculturismo natural. O software oferta diversas funcionalidades focadas no aspecto nutricional e dietético do potencial atleta.

# Manual Build

Passo 1 - Escolha a baseline desejada e clone o repositório para sua máquina local

```
git clone https://github.com/Mel-Rocha/Arnold-Plan/tree/documentation/baseline_3
cd source/source
```

Passo 2 - Instale os módulos via VENV

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Passo 3 - Configure o database

```
python manage.py makemigrations
python manage.py migrate
```

Passo 4 - Crie um superuser

```
python manage.py createsuperuser
```

Passo 5 - Rode a aplicação

```python
python manage.py runserver
```