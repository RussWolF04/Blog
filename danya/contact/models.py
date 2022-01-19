from ckeditor.fields import RichTextField
from django.db import models


# Класс модели обратной связи
class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Форма обратной связи'


# Класс модели контактов
class ContactLink(models.Model):
    icon = models.FileField(upload_to="icon/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мой контакт'
        verbose_name_plural = 'Мои контакты'


# Класс модели страницы о нас
class About(models.Model):
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


# Класс модели изображений страницы о нас
class ImageAbout(models.Model):
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'Изображение обо мне'
        verbose_name_plural = 'Изображине обо мне'


# Класс модели соцю сетей страницы о нас
class Social(models.Model):
    icon = models.FileField(upload_to="icon/")
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'
