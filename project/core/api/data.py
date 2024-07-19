import json
import os

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.conf import settings

from core.app.verifycator import Verificator
from addict import Dict

DATA_FILE_PATH = os.path.join(settings.BASE_DIR, 'core', 'app', 'data', 'counts.json')


class DataManager:
    ...