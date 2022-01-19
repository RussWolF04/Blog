from ckeditor.fields import RichTextField  # Импортируем плагин для редактирования текста в админ панели
from django.contrib.auth.models import User  # Импортируем модель User из Django
from django.db import models
# Библиотека MPTT посзволит нам делать воложенности в Категориях,
# т.е. категория может быть завязана на категорию
from django.urls import reverse
# Импортируем тайм зону
from django.utils import timezone
#
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


# Класс Категорий Постов
class Category(MPTTModel):
    name = models.CharField(max_length=100)  # Имя Категории
    slug = models.SlugField(max_length=100)  #
    # Используем метод Django-MPTT
    # Указываем родительскую Категорию и к какой категории относиться пост
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Класс Тег
class Tag(models.Model):
    name = models.CharField(max_length=150)  # Имя Тега
    slug = models.SlugField(max_length=100, unique=True)  # Делаем slug уникальным

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


# Класс Пост
class Post(models.Model):
    # Автор поста
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # Заголовок поста
    title = models.CharField(max_length=200)  # Заголовок Поста (CharField - строка с ограничениями по символам)
    # Картинка (фото, изображение) поста
    image = models.ImageField(upload_to='articles/')  # upload_to= "указываем куда будутет сохранятья изображение"
    # Текст поста
    # RichTextField (TextField - это поле как и TextField, но с возможностью редактировать текст)
    text = RichTextField()

    # Привязка поста к Категории
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,  # SET_NULL-что бы при удалении категории не удалялись статьи
        null=True
    )
    # Прописываем Теги
    tags = models.ManyToManyField(Tag, related_name="post")  # один ко многим
    # Дата и время создания поста
    create_at = models.DateTimeField(auto_now_add=True)  # Автоматическое подставление даты и время создания поста
    slug = models.SlugField(max_length=200, default='')

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comment.all()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


# Коментарии к Посту
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    message = models.TextField(max_length=500)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'