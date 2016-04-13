import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .forms import RegistrationForm


@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    try:
        payload = json.loads(request.body.decode())
    except ValueError:
        return JsonResponse({'error': 'Unable to parse body'}, status=400)

    form = RegistrationForm(payload)
    if form.is_valid():
        user = User.objects.create_user(form.cleaned_data['username'],
                                        form.cleaned_data['email'],
                                        form.cleaned_data['password'])
        user.save()
        return JsonResponse({"success": "User registered"}, status=201)

    return HttpResponse(
        form.errors.as_json(),
        status=400,
        content_type='application/json'
    )
