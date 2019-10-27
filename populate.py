import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','login_registration.settings')
import django
django.setup()

import faker
fake = faker.Faker()
