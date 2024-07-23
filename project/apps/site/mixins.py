from django.shortcuts import redirect
from core import Config
from django.urls import reverse


class PermissionRequiredMixin:
    required_permission = 'all'

    def dispatch(self, request, *args, **kwargs):
        user = request.session.get('user')
        if not user:
            return redirect('login')

        user_id = user.get('id')
        if self.required_permission == 'all':
            return super().dispatch(request, *args, **kwargs)
        elif self.required_permission == 'owner' and user_id == Config.OWNER_ID:
            return super().dispatch(request, *args, **kwargs)
        elif self.required_permission == 'scenarist' and user_id in Config.SCENARIST_IDS:
            return super().dispatch(request, *args, **kwargs)
        else:
            error_url = reverse(
                'error', kwargs={'message': 'Permission denied'})
            return redirect(error_url)


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if 'user' not in request.session or not request.session.get('access_token'):
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
