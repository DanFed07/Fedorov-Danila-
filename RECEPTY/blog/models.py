from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published_date = models.DateTimeField('Дата публикации', default=timezone.now)
    image = models.ImageField('Изображение', upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_main = models.BooleanField('Главная новость', default=False)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField('Изображение', upload_to='articles_images/', blank=True, null=True)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    views_count = models.IntegerField('Просмотры', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name='Новость', null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField('Текст комментария')
    created_date = models.DateTimeField('Дата создания', default=timezone.now)
    is_approved = models.BooleanField('Одобрен', default=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_date']

    def __str__(self):
        if self.news:
            return f'Комментарий от {self.author.username} к {self.news.title}'
        return f'Комментарий от {self.author.username} к {self.article.title}'