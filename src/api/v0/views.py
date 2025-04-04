from django.contrib.auth import get_user_model, login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

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

