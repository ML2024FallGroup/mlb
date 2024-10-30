from django.http import JsonResponse



def index(request):
     # run.delay()

    return JsonResponse({"message": "Hello, world. You're at the polls index."})