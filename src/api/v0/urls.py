from rest_framework.routers import DefaultRouter

from api.v0.views import LogoutViewSet, LoginModelViewSet, RegisterModelViewSet, ClickerStatsViewSet

router = DefaultRouter()

router.register(r'login', LoginModelViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')
router.register(r'register', RegisterModelViewSet, basename='register')
router.register(r'stats', ClickerStatsViewSet, basename='stats')



urlpatterns = [

]

urlpatterns += router.urls