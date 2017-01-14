import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}
# Add PostGIS engine
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
