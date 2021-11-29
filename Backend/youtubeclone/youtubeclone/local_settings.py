# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=r(=uwwl82ks@af_ne)i@@1crxbr_mh-6d6ww#lh1by82nwbn3'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'eifh0sdjfs-275d',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}