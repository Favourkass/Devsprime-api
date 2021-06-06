from django.http import JsonResponse


def index(request):
    message = 'Welcome to Blog App'
    return JsonResponse(dict(message=message))
