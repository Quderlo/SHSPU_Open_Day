from django.views.generic import TemplateView


class RegistrationView(TemplateView):
    template_name = 'auth/registration.html'