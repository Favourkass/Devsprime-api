from django.http import JsonResponse


def index(request):
    message = 'Welcome to Edu Prime Rest API. Visit /api'
    return JsonResponse(dict(message=message))
