# coding: utf-8

# Adrien Brunet <brunet.adrien@gmail.com>

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todomvc.settings")

application = get_wsgi_application()
