"""
Copyright 2023 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from functools import wraps
from core import Config
from django.shortcuts import redirect
from django.urls import reverse


def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'user' not in request.session:
            return redirect('login')

        access_token = request.session.get('access_token')
        if not access_token:
            return redirect('login')

        return view_func(request, *args, **kwargs)

    return _wrapped_view

def permission_check(required_permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.session.get('user')
            if not user:
                return redirect('login')

            user_id = user.get('id')
            if not user_id:
                return redirect('login')

            if required_permission == 'all':
                return view_func(request, *args, **kwargs)
            elif required_permission == 'owner' and user_id == Config.OWNER_ID:
                return view_func(request, *args, **kwargs)
            elif required_permission == 'scenarist' and user_id in Config.SCENARIST_IDS:
                return view_func(request, *args, **kwargs)
            else:
                error_url = reverse('error', kwargs={'message': 'Permission denied'})
                return redirect(error_url)

        return _wrapped_view
    return decorator