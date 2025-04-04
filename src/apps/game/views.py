from django.contrib.redirects.models import Redirect

def clicker(request):
    if not request.user.is_authenticated:
        pass
        Redirect()

