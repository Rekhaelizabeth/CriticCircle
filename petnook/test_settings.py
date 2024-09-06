# test_settings.py

import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petnook.settings')  # Replace 'myproject' with your project name

print("INSTALLED_APPS:", settings.INSTALLED_APPS)
