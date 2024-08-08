"""
Django settings for faq_backend project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from my_settings import SECRET_KEY, DATABASES

# 프로젝트 내부 경로 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 개발 환경 설정 (프로덕션 환경에서는 적합하지 않음)
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/ 참고

# 프로덕션 환경에서 사용할 경우 비밀키를 꼭 비밀로 유지할 것
SECRET_KEY = SECRET_KEY

# 프로덕션 환경에서 디버그 모드 사용 금지
DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = 'mypage'
LOGIN_URL = 'login'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 애플리케이션 정의

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'faq',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 소셜 계정을 사용할 경우 필요한 provider 추가
    # 예: 'allauth.socialaccount.providers.google',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# 이메일 인증 관련 설정
ACCOUNT_EMAIL_VERIFICATION = "none"  # "optional" 또는 "mandatory"로 변경 가능
ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = 'mypage'
LOGIN_URL = 'login'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # 추가된 미들웨어
]

ROOT_URLCONF = 'faq_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # 이 줄이 필요합니다.
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'faq_backend.wsgi.application'

# 데이터베이스 설정
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/ref/settings/#databases 참고

DATABASES = DATABASES

# 비밀번호 검증
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators 참고

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 국제화 설정
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/topics/i18n/ 참고

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

# 정적 파일 설정 (CSS, JavaScript, Images)
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/howto/static-files/ 참고

STATIC_URL = 'static/'

# 기본 기본 키 필드 유형
# 자세한 내용은 https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field 참고

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
