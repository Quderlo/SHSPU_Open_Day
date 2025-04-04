from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)
        extra_kwargs = {
            'username': {
                'required': True,
                'error_messages': {
                    'blank': 'Пожалуйста, заполните поле имени',
                }
            },

            'password': {
                'required': True,
                'write_only': True,
                'error_messages': {
                    'blank': 'Пожалуйста, заполните поле пароля.',
                }
            },
        }

    def validate(self, data):
        username = data['username']
        username = data['password']

        return data


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, error_messages={
        "required": "Пожалуйста, напишите ваше имя пользователя.",
        "blank": "Пожалуйста, напишите ваше имя пользователя.",
        "invalid": "Пожалуйста, введите корректное имя пользователя.",
    })

    password = serializers.CharField(write_only=True, required=True, error_messages={
        "required": "Пожалуйста, напишите ваш пароль.",
        "blank": "Пожалуйста, напишите ваш пароль.",
    })

    class Meta:
        model = User
        fields = ('username', 'password', )


    def validate(self, data):
        username = data['username']
        password = data['password']

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Пользователь с таким именем не существует.'})

        user = User.objects.get(username=username)

        if not user.check_password(password):
            raise serializers.ValidationError({'password': 'Не верный пароль.'})

        data['user'] = user
        return data


    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])

        if not user:
            raise serializers.ValidationError({'password': 'Не верный пароль.'})

        return user




class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', '')