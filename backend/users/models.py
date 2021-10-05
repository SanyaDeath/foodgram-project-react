from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True, blank=False)
    bio = models.TextField(blank=True)
    username = models.CharField(unique=True, blank=False, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('username',)

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Пользователь подписчик')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Пользователь на которого подписываемся')
    created_at = models.DateTimeField(
        auto_now_add=True, null=True, verbose_name='Время создания'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_follow'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.author}'
