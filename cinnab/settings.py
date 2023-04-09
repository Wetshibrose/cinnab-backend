from pathlib import Path
from decouple import config

from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", cast=str)

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = [config("ALLOWED_HOSTS_A", cast=str), config("ALLOWED_HOSTS_B", cast=str)]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    # third party apps
    "django_crontab",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "corsheaders",
    "django_filters",
    # apps
    "account.apps.AccountConfig",
    "ads.apps.AdsConfig",
    "authentication.apps.AuthenticationConfig",
    "businesses.apps.BusinessesConfig",
    "categories.apps.CategoriesConfig",
    "currencies.apps.CurrenciesConfig",
    "customers.apps.CustomersConfig",
    "faqs.apps.FaqsConfig",
    "languages.apps.LanguagesConfig",
    "locations.apps.LocationsConfig",
    "menu.apps.MenuConfig",
    "notifications.apps.NotificationsConfig",
    "orders.apps.OrdersConfig",
    "payment_methods.apps.PaymentMethodsConfig",
    "products.apps.ProductsConfig",
    "reports.apps.ReportsConfig",
    "settings.apps.SettingsConfig",
    "shopping_cart.apps.ShoppingCartConfig",
    "theme.apps.ThemeConfig",
    "users.apps.UsersConfig",
    "wishlist.apps.WishlistConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # ----------corsheaders--------------
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# cors settings
CORS_ALLOW_ALL_ORIGINS=config("CORS_ALLOW_ALL_ORIGINS", cast=bool)

# rest framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "users.backends.PhoneNumberBackend",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

# simple jwt settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": config("JWT_SECRET_KEY", cast=str),
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": config("JWT_LEEWAY", cast=int),

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

ROOT_URLCONF = "cinnab.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cinnab.wsgi.application"


# postgres setup
DATABASES = {
    "default": {
        "ENGINE": config("PG_ENGINE", cast=str),
        "NAME": config("PG_NAME", cast=str),
        "USER": config("PG_USER", cast=str),
        "PASSWORD": config("PG_PASSWORD", cast=str),
        "HOST": config("PG_HOST", cast=str),
        "PORT": config("PG_PORT", cast=int),
    }
}

# password validators settings
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = ["users.backends.PhoneNumberBackend", "django.contrib.auth.backends.ModelBackend",]
AUTH_USER_MODEL = "users.User"

# time and languages settings
LANGUAGE_CODE = config("LANGUAGE_CODE", cast=str)

TIME_ZONE = config("TIME_ZONE", cast=str)

USE_I18N = config("USE_I18N", cast=bool)

USE_TZ = config("USE_TZ", cast=bool)


# Static settings
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# gdal settings
GDAL_LIBRARY_PATH = r'C:\\OSGeo4W\bin\\gdal306.dll'