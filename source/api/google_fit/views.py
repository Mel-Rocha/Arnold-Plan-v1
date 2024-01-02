import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def google_fit_auth(request):
    # Caminho absoluto para o diretório raiz do projeto Django
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Caminho para o arquivo de credenciais do cliente (client_secret.json)
    CLIENT_SECRET_PATH = os.path.join(BASE_DIR, 'client_secret.json')
    
    # Scopes necessários para a API do Google Fit
    SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']

    # Caminho para o arquivo de token (onde as credenciais serão armazenadas)
    TOKEN_PATH = 'caminho/para/token.json'

    # Configurar o fluxo OAuth
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_PATH,
        scopes=SCOPES,
        redirect_uri='http://127.0.0.1:8000/'
    )

    # Carregar as credenciais existentes se estiverem disponíveis
    credentials = None
    if os.path.exists(TOKEN_PATH):
        credentials = flow.credentials

    # Se as credenciais não existirem ou estiverem expiradas, iniciar o fluxo de autorização
    if not credentials or not credentials.valid:
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        return redirect(authorization_url)
    else:
        # As credenciais são válidas, faça o que for necessário com elas
        # Por exemplo, você pode passá-las para outro método que interage com a API do Google Fit
        return render(request, 'google_fit_auth.html')
