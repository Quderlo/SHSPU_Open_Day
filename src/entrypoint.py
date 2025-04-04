import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def add_super_user():
    user, created = User.objects.get_or_create(
        username='root',
        defaults={'is_superuser': True, 'is_staff': True}
    )
    if created:
        user.set_password('root')
        user.save()
        print(f'Супер пользователь {user.username} создан!')
    else:
        print('Супер пользователь уже существует')


if __name__ == '__main__':
    add_super_user()
    print("Инициализация завершена успешно!")