from django.views.generic import TemplateView

class ClickerGameView(TemplateView):
    template_name = 'game/clicker.html'
