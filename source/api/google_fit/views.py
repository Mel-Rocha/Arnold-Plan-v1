import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from google.oauth2.credentials import Credentials
from api.user_credentials.models import UserCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from django.http import HttpResponseRedirect


"""
configura e inicia o fluxo de autorização OAuth 2.0. Quando o usuário acessa
essa rota, ele é redirecionado para a página de autorização do Google, 
onde pode conceder permissões ao aplicativo.
"""
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
    

@login_required
def test_api_request(request):
    user_credentials, created = UserCredentials.objects.get_or_create(user=request.user)
    credentials_json = user_credentials.credentials_json
    credentials = Credentials.from_authorized_user_info(credentials_json)

    drive = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    files = drive.files().list().execute()

    # Salvar as credenciais de volta na sessão, caso o token de acesso seja atualizado
    user_credentials.credentials_json = credentials.to_json()
    user_credentials.save()

    return JsonResponse(files)


@login_required
def oauth2callback(request):
    # Especifique o estado ao criar o fluxo no retorno, para que ele possa ser
    # verificado na resposta do servidor de autorização.
    state = request.session['state']

    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_PATH, scopes=SCOPES, state=state)
    flow.redirect_uri = request.build_absolute_uri('/oauth2callback')

    # Use a resposta do servidor de autorização para buscar os tokens OAuth 2.0.
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    # Armazene as credenciais no banco de dados associadas ao usuário logado
    user_credentials, created = UserCredentials.objects.get_or_create(user=request.user)
    credentials = flow.credentials
    user_credentials.credentials_json = credentials.to_json()
    user_credentials.save()

    return HttpResponseRedirect('/test_api_request')  # ajuste conforme necessário