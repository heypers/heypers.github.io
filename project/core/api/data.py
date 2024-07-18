import json
import os

from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.conf import settings

from core.app.verifycator import Verificator
from addict import Dict

DATA_FILE_PATH = os.path.join(settings.BASE_DIR, 'core', 'app', 'data', 'counts.json')


class DataManager:
    @staticmethod
    def get_locale(request):
        return request.GET.get('lang', 'en')

    @staticmethod
    def get_data():
        try:
            with open(DATA_FILE_PATH, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {"server_count": 0, "user_count": 0}

    @staticmethod
    def update_data(new_data):
        try:
            os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)
            with open(DATA_FILE_PATH, 'w') as json_file:
                json.dump(new_data, json_file, indent=4)
            return {"status": "success"}, 200
        except Exception as e:
            print(f"Error: {e}")
            return {"status": "failure", "error": str(e)}, 500

    @staticmethod
    def verify_request_token(request):
        token = request.headers.get('X-Auth-Token')
        if not token or not Verificator.verify_token(token):
            return HttpResponseBadRequest('Invalid or missing token')

    @staticmethod
    def get_lines(lang, to_localize):
        try:
            with open(os.path.join(settings.BASE_DIR, 'locale', f"{lang}.json"), encoding='utf-8') as f:
                c = Dict(json.load(f))
            d = to_localize.split('.')
            a = c
            for E in d:
                a = getattr(a, E)
            return a
        except Exception as e:
            raise ValueError(f"Invalid localization key {to_localize} for language {lang}: {e}")


@require_http_methods(['GET', 'POST'])
def api_data_counter(request):
    error_response = DataManager.verify_request_token(request)
    if error_response:
        return error_response

    if request.method == 'POST':
        data = json.loads(request.body)
        if not data:
            return HttpResponseBadRequest('Invalid data')
        response_data, status = DataManager.update_data(data)
        return JsonResponse(response_data, status=status)
    else:
        data = DataManager.get_data()
        return JsonResponse(data, status=200)
