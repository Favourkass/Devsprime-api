from django.http import JsonResponse


def index(request):
    message = 'Welcome to DevsPrime Rest API. Visit /api'
    return JsonResponse(dict(message=message))
