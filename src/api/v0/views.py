from django.contrib.auth import get_user_model, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from apps.game.models import ClickerStats
from apps.game.serializers import ClickerStatsSerializer
from apps.user.serializers import UserRegisterSerializer, UserLoginSerializer

User = get_user_model()

# Create your views here.
class LoginModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.none()
    http_method_names =  ['head', 'options', 'post']
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({
                'status': 'Вы уже вошли в систему'},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            login(self.request, serializer.validated_data['user'])
            return Response({'status': 'Успешная авторизация'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'head', 'options', 'list']

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return Response(
                {'status': 'Вы успешно вышли из системы'},
                status=status.HTTP_200_OK
            )

        return Response(
            {'status': 'Вы не вошли в систему'},
            status=status.HTTP_403_FORBIDDEN
        )


class RegisterModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.none()
    http_method_names = ['head', 'options', 'post']
    serializer_class = UserRegisterSerializer


# Игровая реализация
class ClickerStatsViewSet(viewsets.ModelViewSet):
    serializer_class = ClickerStatsSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'options', 'post', 'head', 'patch']

    def get_queryset(self):
        return ClickerStats.objects.filter(player=self.request.user)

    def patch(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def click(self, request):
        stats = self.get_queryset().first()
        stats.money += stats.click_power
        stats.total_clicks += 1
        stats.save()
        return Response(self.get_serializer(stats).data)