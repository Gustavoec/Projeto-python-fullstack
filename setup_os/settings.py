from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-sua-chave-secreta-aqui'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'jazzmin', # <-- Tem de ficar acima do admin!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chamados',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup_os.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup_os.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações visuais do Painel Administrativo (Jazzmin)
JAZZMIN_SETTINGS = {
    "site_title": "HelpDesk OS Admin",
    "site_header": "HelpDesk OS",
    "site_brand": "🛠️ HelpDesk OS",
    "welcome_sign": "Bem-vindo ao Painel de Controle, Gustavo",
    "copyright": "HelpDesk OS - Portfólio",

    # Ícones para os modelos do menu lateral (usando FontAwesome)
    "icons": {
        "auth.user": "fas fa-user-shield",
        "auth.Group": "fas fa-users",
        "chamados.cliente": "fas fa-user-tie",
        "chamados.ordemservico": "fas fa-tools",
    },

    # Modelo de UI customizável
    "show_sidebar": True,
    "navigation_expanded": True,
}
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'chamados.context_processors.admin_dashboard_metrics', # <-- Adicione esta linha aqui!
            ],
        },
    },
]
JAZZMIN_SETTINGS = {
    "site_title": "HelpDesk OS Admin",
    "site_header": "HelpDesk OS",
    "site_brand": "🛠️ HelpDesk OS",
    "welcome_sign": "Bem-vindo ao Painel de Controle, Gustavo",
    "copyright": "HelpDesk OS - Portfólio",

    # Ícones para os modelos do menu lateral
    "icons": {
        "auth.user": "fas fa-user-shield",
        "auth.Group": "fas fa-users",
        "chamados.cliente": "fas fa-user-tie",
        "chamados.ordemservico": "fas fa-tools",
    },

    "show_sidebar": True,
    "navigation_expanded": True,

    # --- ADICIONA ESTE BLOCO PARA CRIAR O LINK DA DASHBOARD NO MENU DO ADMIN ---
    "custom_links": {
        "chamados": [{
            "name": "📊 Dashboard Gráfica",
            "url": "/dashboard/",
            "icon": "fas fa-chart-pie",
            "permissions": ["chamados.view_ordemservico"]
        }]
    },
}
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'helpdesk_db'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'sua_senha_segura'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}