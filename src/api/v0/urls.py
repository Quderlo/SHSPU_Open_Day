from rest_framework.routers import DefaultRouter

from api.v0.views import LogoutViewSet, LoginModelViewSet, RegisterModelViewSet

router = DefaultRouter()

router.register(r'login', LoginModelViewSet, basename='login')
router.register(r'logout', LogoutViewSet, basename='logout')
router.register(r'register', RegisterModelViewSet, basename='register')

urlpatterns = [

]

urlpatterns += router.urls