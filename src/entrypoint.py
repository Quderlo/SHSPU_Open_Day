import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

def add_super_user():
    user = User.objects.create_superuser(
        username='root',
        password='root',
    )

    print(f'Супер пользователь {user.username} создан!')


add_super_user()