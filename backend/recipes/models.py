from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Имя ингредиента')
    measure_unit = models.CharField(max_length=20,
                                    verbose_name='Единица измерения')

    class Meta:
        ordering = ['name', ]
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name} {self.measure_unit}'


class Tag(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='Имя тега')
    color = models.CharField(max_length=8,
                             verbose_name='Цвет')
    slug = models.SlugField(verbose_name='слаг')

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='автор'
                               )
    name = models.CharField(max_length=200,
                            verbose_name='Название рецепта')
    image = models.ImageField(upload_to='recipes/images',
                              verbose_name='Изображение',)
    text = models.TextField(max_length=1280,
                            verbose_name='Способ приготовления')
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredient',
                                         verbose_name='Ингредиенты')
    tags = models.ManyToManyField(Tag, through='RecipeTag',
                                  verbose_name='Теги')
    cooking_time = cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), ],
        verbose_name='Время приготовления')
    pub_date = models.DateTimeField(verbose_name='Дата добавления',
                                    auto_now_add=True,
                                    db_index=True,
                                    slug=models.SlugField(verbose_name='слаг'))

    class Meta:
        ordering = ('name', 'pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.author}: {self.name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество')

    class Meta:
        verbose_name = 'Ингредиенты'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ingredient}: {self.amount}'


class RecipeTag(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE,
                            verbose_name='Тег')

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.tag}'


class Follow(models.Model):
    user = models.ForeignKey(User,
                             verbose_name='Подписчик',
                             on_delete=models.CASCADE,
                             related_name='follower')
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               on_delete=models.CASCADE,
                               related_name='following')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')

    class Meta:
        ordering = ['created']
        verbose_name = 'Подписка'
        verbose_name = 'Подписки'
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'],
            name='unique_follow')]

    def __str__(self):
        return f'{self.user} following {self.author}'


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='favorites',
                             )
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт',
                               related_name='favorites',
                               )
    added_date = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Избранные'
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'],
            name='unique_favorite')]

    def __str__(self):
        return f'{self.user} added {self.recipe}'


class Shopping(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping',
        verbose_name='Рецепт'
    )
    added_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        constraints = [models.UniqueConstraint(
            fields=['user', 'recipe'],
            name='unique_shopping')]

    def __str__(self):
        return f'{self.user} added {self.recipe}'
